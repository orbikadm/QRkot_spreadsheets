from datetime import datetime
from typing import Union

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.donation import Donation
from app.models.charity_project import CharityProject
from app.core.db import get_async_session


def close_obj(obj):
    obj.invested_amount = obj.full_amount
    obj.fully_invested = True
    obj.close_date = datetime.now()


async def investment_process(
        obj_in: Union[CharityProject, Donation],
        session: AsyncSession = Depends(get_async_session)
) -> None:

    obj_db_model = CharityProject if isinstance(obj_in, Donation) else Donation

    objs_db = await session.execute(
        select(obj_db_model)
        .where(obj_db_model.fully_invested == 0)
        .order_by(obj_db_model.create_date)
    )

    objs_db = objs_db.scalars().all()

    if not objs_db:
        return obj_in

    for obj_db in objs_db:
        need_money = obj_db.full_amount - obj_db.invested_amount
        available = obj_in.full_amount - obj_in.invested_amount

        if need_money > available:
            obj_db.invested_amount += available
            close_obj(obj_in)

        elif need_money == available:
            close_obj(obj_in)
            close_obj(obj_db)

        else:
            obj_in.invested_amount += need_money
            close_obj(obj_db)

        session.add(obj_db)

    session.add(obj_in)
    await session.commit()
    await session.refresh(obj_in)
    return obj_in
