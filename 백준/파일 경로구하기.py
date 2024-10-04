import pandas as pd

# CSV 파일 경로 설정 (적절한 방법 선택)
file_path = r"C:\Users\sickt\OneDrive\Desktop\korea_floating_population_data.csv"  # 방법 3 사용

# CSV 파일을 pandas DataFrame으로 불러오기
try:
    df = pd.read_csv(file_path, encoding='cp949')
    print("파일이 성공적으로 불러와졌습니다.")
    # DataFrame의 첫 몇 행을 출력하여 데이터 확인
    print(df.head())
except FileNotFoundError:
    print("파일을 찾을 수 없습니다. 경로를 확인하세요.")
except Exception as e:
    print(f"파일을 불러오는 중 오류가 발생했습니다: {e}")
