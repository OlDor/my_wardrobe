from fastapi import FastAPI
from pydantic import BaseModel

# 1. Ваш класс с логикой
class Calculator:
    def add(self, a: float, b: float):
        return a + b

# 2. Описание структуры входных данных (JSON)
class Numbers(BaseModel):
    a: float
    b: float

# 3. Инициализация приложения и класса
app = FastAPI()
calc = Calculator()

# 4. Создание эндпоинта
@app.post("/add")
async def calculate_sum(data: Numbers):
    result = calc.add(data.a, data.b)
    return {"sum": result}

if __name__ == "__main__":
    import uvicorn
    # Запускаем на порту 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)