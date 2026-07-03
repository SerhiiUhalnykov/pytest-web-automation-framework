from pathlib import Path
from datetime import datetime
import shutil

import pytest

from utils.logger import get_logger
from utils.config import settings
from utils.workers import get_worker_id

logger = get_logger(__name__)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item):
    """Hook that generates a report status each test for failure handling."""

    outcome = yield
    report: pytest.TestReport = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


def pytest_sessionfinish(session: pytest.Session) -> None:
    """Drop categories.json into the Allure results dir so the report picks it up."""

    alluredir = session.config.getoption("allure_report_dir", default=None)
    if not alluredir:
        return
    src = Path(__file__).parent / "categories.json"
    dst = Path(alluredir) / "categories.json"
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dst)


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    """Deselect demo tests unless the run explicitly asks for them via -m demo."""

    if "demo" in (config.getoption("markexpr") or ""):
        return
    selected, deselected = [], []
    for item in items:
        target = deselected if item.get_closest_marker("demo") else selected
        target.append(item)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected


@pytest.fixture(scope="module")
def artifacts_dir(artifacts_subdir: str) -> Path:
    """Create a directory to store test artifacts."""

    art_dir = Path(settings.artifacts_dir) / artifacts_subdir
    art_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Artifacts dir: {art_dir}")

    return art_dir


@pytest.fixture(scope="function")
def artifacts_path(
    artifacts_dir: Path,
    request: pytest.FixtureRequest,
) -> Path:
    """Create names and paths for test artifacts."""

    worker = get_worker_id()
    name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return artifacts_dir / f"{worker}_{name}_{timestamp}"
