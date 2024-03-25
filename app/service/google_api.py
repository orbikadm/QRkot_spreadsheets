from app.constants import create_table_body, create_table_head
from app.core.config import settings
from app.core.google_client import Aiogoogle


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    service = await wrapper_services.discover('sheets', 'v4')
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=create_table_body())
    )
    return response['spreadsheetId']


async def set_user_permissions(
    spreadsheetid: str,
    wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        )
    )


async def spreadsheets_update_value(
        spreadsheetid: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = create_table_head()
    for project in projects:
        new_line = [
            str(project.name),
            str(project.close_date - project.create_date),
            str(project.description)
        ]
        table_values.append(new_line)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range='Лист1!A1:E30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
