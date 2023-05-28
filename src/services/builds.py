from fastapi import HTTPException

from dto.builds import BuildDTO


class BuildService:
    @staticmethod
    async def get_build(build_name: str, builds: dict[str, BuildDTO]) -> BuildDTO:
        if build_name not in builds:
            raise HTTPException(status_code=404, detail=f"Build {build_name} not found")
        return builds.get(build_name)
