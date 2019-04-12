"""
Internal api methods for current service.

Example:

    from anthill.platform.api.internal import as_internal, InternalAPI

    @as_internal()
    async def your_internal_api_method(api: InternalAPI, *params, **options):
        # current_service = api.service
        ...
"""
from anthill.platform.api.internal import as_internal, InternalAPI
from moderation.models import ModerationAction


@as_internal()
async def get_moderations(api: InternalAPI, user_id: str) -> dict:
    objects = ModerationAction.actions_query(user_id).all()
    result = ModerationAction.dump_many(objects).data
    return result
