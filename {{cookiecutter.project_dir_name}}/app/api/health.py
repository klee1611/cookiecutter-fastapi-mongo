from fastapi import APIRouter

router = APIRouter()


@router.get('/', include_in_schema=False)
@router.get('')
async def health():
    return {}
