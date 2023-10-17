from fastapi import APIRouter
from ports.inbound.person_crud_port import PersonCrudPort

router = APIRouter()

person_crud_port = PersonCrudPort()


@router.post('/new_person', response_model=dict)
async def new_person(person_data: dict):
    try:
        # Create a new person and return your ID.
        person = person_crud_port.create_person(person_data)
        return person
    except Exception as exception:
        return exception


@router.get('/hello')
async def read_root():
    return {"Hello": "World"}


@router.get('/tables')
async def get_tables():
    try:
        tables = person_crud_port.show_tables()
        return tables

    except Exception as exception:
        return exception

