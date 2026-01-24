from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "R59N106BKDD"
options.udid = "R59N106BKDD"
options.automation_name = "UiAutomator2"
options.no_reset = True
options.dont_stop_app_on_reset = True

appium_server_url = "http://127.0.0.1:4723/wd/hub"
driver = webdriver.Remote(command_executor=appium_server_url, options=options)
wait = WebDriverWait(driver, 7)

# 화면 크기 가져오기
size = driver.get_window_size()
start_x = size['width'] * 0.5
start_y = size['height'] * 0.8
end_y = size['height'] * 0.2


# 클릭 + 화면(진입/노출) 검증
def click_and_verify(title, click_locator, verify_locator):
    try:
        wait.until(EC.element_to_be_clickable(click_locator)).click()
        wait.until(EC.visibility_of_element_located(verify_locator))
        print(f"✅ {title} \n")

    except TimeoutException:
        print(f"❌ {title} \n")
        raise


# 클릭 검증
def click_only(title, locator):
    try:
        wait.until(EC.element_to_be_clickable(locator)).click()
        print(f"✅ {title} \n")
    except TimeoutException:
        print(f"❌ {title} \n")
        raise     


# 화면(진입/노출) 검증
def verify_only(title, locator):
    try:
        wait.until(EC.visibility_of_element_located(locator))
        print(f"✅ {title} \n")
    except TimeoutException:
        print(f"❌ {title} \n")
        raise  


# 텍스트 입력
def input_text(title, locator, value):
    try:
        el = wait.until(EC.element_to_be_clickable(locator))
        el.send_keys(value)
        print(f"✅ {title} 입력 \n")

    except TimeoutException:
        print(f"❌ {title} 입력 실패\n")
        raise

# Toast 메시지
def verify_toast_only(title, locator):
    try:
        wait.until(EC.presence_of_element_located(locator))
        print(f"✅ {title}\n")
    except TimeoutException:
        print(f"❌ {title}\n")
        raise
 
 
# 텍스트 추출 
def get_broadcast_name(parent_locator, index=0,):
    parent = wait.until(EC.visibility_of_element_located(parent_locator))
    text_els = parent.find_elements(By.CLASS_NAME, "android.widget.TextView")
    return text_els[index].get_attribute("text")
 
     

# TC-005 상단 카테고리 탭 기능 확인 --------------------------------------------------------------------------------------------------

try:
    
    click_and_verify(
       "게임 카테고리 탭 진입 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("게임")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("게임 카테고리")'))
        
        
    click_and_verify(
       "보이는 라디오 카테고리 탭 진입 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("보이는 라디오")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("보이는 라디오 전체")'))


    click_and_verify(
       "스포츠 탭 진입 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("스포츠")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("스포츠 카테고리")'))

    
    click_and_verify(
       "전체 탭 진입 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("전체")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("LIVE 전체")'))
    


# TC-006 라이브 탭 More 메뉴 기능 확인 --------------------------------------------------------------------------------------------------    
    
    click_only(
       "라이브 탭 More 메뉴",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().description("더보기").instance(0)'))

    # 스트리머 명 
    broadcast_name = get_broadcast_name(
    (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(6)'))
    print(broadcast_name)
    
    
    click_only(
       "방송국 가기",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(6)'))
    
    
    time.sleep(7)
    
    # 스트리머 명 
    broadcast_name2 = get_broadcast_name(
    (By.XPATH,'//android.view.View[@resource-id="main"]/android.view.View[2]/android.view.View[2]'))
    print(broadcast_name2) 
    
    
    # 스트리머 명 비교
    base = broadcast_name.replace(" 방송국 가기", "")
    if base == broadcast_name2:
     print("✅ 스트리머 명 일치 \n")
    else:
     print("❌ 스트리머 명 불일치")
    
    
    click_only(
       "CLOSE",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("kr.co.nowcom.mobile.afreeca:id/inapp_webview_close_btn")'))
    
    
    click_only(
       "라이브 탭 More 메뉴",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().description("더보기").instance(0)')) 
    
    
    click_only(
       "나중에 보기",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("나중에 보기")'))
    
    verify_toast_only(
       "나중에 보기 (TC Result)",
       (By.XPATH, "//android.widget.Toast[@text='이미 나중에 보기에 추가됐습니다.']"))
    
   
    click_only(
       "라이브 탭 More 메뉴",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().description("더보기").instance(0)')) 
    
    
    click_and_verify(
       "공유하기 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("공유하기")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("Quick Share")'))
    
    
    # Back
    driver.press_keycode(4)
    
    
    
# TC-007 라이브 탭 More 메뉴 기능 확인 (2) --------------------------------------------------------------------------------------------------    
    
    click_only(
       "라이브 탭 More 메뉴",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().description("더보기").instance(0)'))
    
    
    click_only(
       "즐겨찾기 추가",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("즐겨찾기 추가")'))
    
    
    verify_toast_only(
       "즐겨찾기 추가 (TC Result)",
       (By.XPATH, "//android.widget.Toast[@text='이미 즐겨찾기 되어있는 스트리머입니다.']"))
    
    
    click_only(
       "라이브 탭 More 메뉴",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().description("더보기").instance(0)'))
    
    
    click_and_verify(
       "스트리머 숨기기 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("스트리머 숨기기")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("실행취소")'))
    
    
    click_only(
       "CLOSE",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("실행취소")'))
    
    
    click_only(
       "라이브 탭 More 메뉴",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().description("더보기").instance(0)'))
    
    
    click_and_verify(
       "신고하기 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("신고하기")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("도박")'))
    
    
    click_only(
       "CLOSE",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("page_close")')) 
    
     
finally:
    driver.quit()

    