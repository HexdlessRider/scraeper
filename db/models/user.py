from db.db_connection import lifespan


class UserStore:
    @staticmethod
    async def get_user_by_id(user_id: int):
        async with lifespan() as client:
            user = await client.table("profiles").select("*").eq("id", user_id).execute()
            return user.data[0]
