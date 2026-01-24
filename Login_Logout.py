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
wait = WebDriverWait(driver, 5)

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
 
     


# TC-001 로그인 기능 확인 (Fail Case) --------------------------------------------------------------------------------------------------

try:
    
    click_and_verify(
      "더보기 탭 진입 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("kr.co.nowcom.mobile.afreeca:id/navigation_more")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("콘텐츠").instance(0)'))
        
        
    click_and_verify(
       "로그인 화면 진입 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그인")'),
       (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("로그인 후 더 많은 서비스를 즐겨보세요.")'))


    input_text(
       "ID",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("아이디")'),
       "erick1")
    
    
    click_and_verify(
       "로그인 버튼 선택-ID만 입력 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그인")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("비밀번호를 입력해주세요.")'))
    
    
    # ID 초기화
    ID_B = wait.until(EC.element_to_be_clickable((By.ANDROID_UIAUTOMATOR,'new UiSelector().text("erick1")'))) 
    ID_B.clear()


    input_text(
       "PW",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("비밀번호")'),
       "lch00810@@")
    
    
    click_and_verify(
       "로그인 버튼 선택-PW만 입력 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그인")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("아이디를 입력해주세요.")'))
    
    
    # PW 초기화
    PW_B = wait.until(EC.element_to_be_clickable((By.ANDROID_UIAUTOMATOR,'new UiSelector().text("••••••••••")'))) 
    PW_B.clear()
    
    
    input_text(
       "ID",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("아이디")'),
       "dasjwdkokodksadwwdwds")


    input_text(
       "PW",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("비밀번호")'),
       "lch00810!!!!!!!!!!!!!!")
    
    
    click_and_verify(
       "로그인 버튼 선택-ID, PW 입력 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그인")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("등록되지 않은 아이디이거나, 아이디 또는 비밀번호를 잘못 입력하셨습니다.")'))
    
    
    click_and_verify(
       "X 버튼 선택 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Button").instance(0)'),
       (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("로그인")'))
    



# TC-002 로그인 기능 확인 (Success Case) --------------------------------------------------------------------------------------------------

    click_only(
       "로그인 화면 진입",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그인")'))
       
    
    input_text(
       "ID",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("아이디")'),
       "erick1")


    input_text(
       "PW",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("비밀번호")'),
       "lch00810@@")
    

    click_and_verify(
       "로그인 버튼 선택-2차 비밀번호 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그인")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("2차 비밀번호 찾기")'))
    

    input_text(
       "2차 비밀번호",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("2차 비밀번호")'),
       "qwer123412")
    

    click_and_verify(
       "최종 로그인 완료 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그인")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("erick1")'))




# TC-003 로그아웃 기능 확인 --------------------------------------------------------------------------------------------------

    click_and_verify(
       "> 버튼 선택 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(16)'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("애드벌룬")')) 
    
    
    # 아래로 스와이프
    driver.swipe(start_x, start_y, start_x, end_y, 500)
    
    
    click_and_verify(
       "로그아웃 버튼 선택 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그아웃")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("방송 참여를 통해 좋아하는 스트리머를 발견해보세요.")'))  
     
    
    click_and_verify(
       "더보기 탭 진입 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("kr.co.nowcom.mobile.afreeca:id/navigation_more")'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그인 해주세요.")'))
    
 
 
    
# TC-004 소셜 로그인 기능 확인 --------------------------------------------------------------------------------------------------  

    click_only(
       "로그인 화면 진입",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("로그인")'))
    
    
    verify_only(
        "트위치 소셜 로그인 아이콘 확인 (TC Result)",
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(6)'))
    
    
    verify_only(
        "네이버 소셜 로그인 아이콘 확인 (TC Result)",
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(8)'))


    verify_only(
        "카카오 소셜 로그인 아이콘 확인 (TC Result)",
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(10)'))


    verify_only(
        "애플 소셜 로그인 아이콘 확인 (TC Result)",
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(12)'))
    
    
    click_and_verify(
       "네이버 소셜 로그인 (TC Result)",
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(8)'),
       (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("erick1")'))
    
     
     
finally:
    driver.quit()

    