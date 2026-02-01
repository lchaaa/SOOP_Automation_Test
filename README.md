# 💡 Topic

- SOOP 모바일 서비스 Login / Logout 기능 자동화 테스트 구현
- SOOP 모바일 서비스 Live Tab 기능 자동화 테스트 구현
- SOOP 모바일 서비스 테스트를 자동화하여 회귀 테스트 효율성 및 품질 안정성 확보

---

# 📝 Function

- 클릭, 입력, 텍스트 추출, 화면(진입/노출) 검증 등 반복되는 테스트 동작을 공통 함수로 분리하여 코드 재사용성과 유지보수성 향상
- 동적으로 변경되는 텍스트를 안정적으로 검증하기 위해 상위 컨테이너 기준으로 하위 TextView를 탐색하여 텍스트 추출 로직 구현
- `try-except (TimeoutException)` 기반 예외 처리로 성공/실패 시나리오를 명확히 분리하고 테스트 결과 판별 기준 체계화
- `WebDriverWait`과 `time.sleep`을 활용한 대기 처리로 데이터 로딩 지연에 대응하여 테스트 안정성 및 재현성 확보
- 사전에 설계된 자동화 테스트 케이스를 기반으로 스크립트를 구현하여 검증 프로세스의 효율성 및 일관성 향상

---

# 🛠 Next

- TC-008 라이브 탭 필터 기능 자동화 테스트
- TC-009 라이브 방송 시청 기능 자동화 테스트
- SOOP 모바일 서비스 MY Tab 기능 자동화 테스트 구현

---

# ✏ Test Case

- Test Case 문서  
  - [SOOP Automation Test TC.xlsx](SOOP_Automation_Test_TC.xlsx)
  - Google Sheets  
    https://docs.google.com/spreadsheets/d/1WPIoh1C1RvmCUc2l651q369Dh9EwkBabVmlzcE_wcp0/edit?usp=sharing

---

# 📷 Video

- 자동화 테스트 실행 영상 추후 업데이트 예정
