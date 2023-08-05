from typing import Optional
from datetime import datetime
from .base_manager import BaseManager
from .models import Check, CheckExecution
from .utils.sessions import session_scope


class CheckExecutionManager(BaseManager):
    @staticmethod
    def create_check_execution(
        check: Check,
        status: Optional[str] = None,
        params: Optional[str] = None,
        logs: Optional[str] = None,
        traceback: Optional[str] = None,
        exception: Optional[str] = None,
    ) -> CheckExecution:
        new_execution = CheckExecution.create(
            check=check,
            status=status,
            params=params,
            logs=logs,
            traceback=traceback,
            exception=exception,
        )
        with session_scope() as session:
            session.add(new_execution)

        return new_execution

    @staticmethod
    def update_execution(
        execution_id: int,
        finished_at: datetime = datetime.now(),
        status: Optional[str] = None,
        params: Optional[str] = None,
        logs: Optional[str] = None,
        traceback: Optional[str] = None,
        exception: Optional[str] = None,
    ):
        with session_scope() as session:
            session.query(CheckExecution).filter_by(id=execution_id).update(
                {
                    "status": status,
                    "params": params,
                    "logs": logs,
                    "traceback": traceback,
                    "exception": exception,
                    "finished_at": finished_at,
                }
            )
