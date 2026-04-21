print("conftest loaded")
import pytest
from playwright.sync_api import sync_playwright
from pytest_html import extras 

@pytest.fixture
def custom_page(request):
    p = sync_playwright().start()

    
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
            record_video_dir="videos",
            record_video_size={"width": 1280, "height": 720}
        )

    page = context.new_page()

    yield page

    print("After test execution")

    if request.node.rep_call.failed:
           page.screenshot(path=f"screenshots/{request.node.name}.png")

    
    context.close()
    browser.close()
    p.stop()

from pytest_html import extras

from pytest_html import extras

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)

    if report.when == "call":
        extras_list = []

        if report.failed:
            screenshot_path = f"screenshots/{item.name}.png"

            extras_list.append(extras.image(screenshot_path))

        extras_list.append(
            extras.html('<a href="videos" target="_blank">View Video</a>')
        )

        if hasattr(report, "extras"):
            report.extras.extend(extras_list)
        else:
            report.extras = extras_list
            