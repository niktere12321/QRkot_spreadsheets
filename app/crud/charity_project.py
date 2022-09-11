from typing import List

from app.crud.base import BaseCRUD
from app.models.charity_project import CharityProject
from sqlalchemy import func, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDCharityProject(BaseCRUD):

    async def get_charity_project_by_name(
        self,
        charity_project_name: str,
        session: AsyncSession
    ):
        charity_project = await session.scalar(
            select(self.model).where(
                self.model.name == charity_project_name
            )
        )
        return charity_project

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession,
    ) -> List[CharityProject]:
        projects: Result = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            ).order_by(
                func.julianday(CharityProject.close_date) -
                func.julianday(CharityProject.create_date)
            )
        )
        projects = projects.scalars().all()
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)
