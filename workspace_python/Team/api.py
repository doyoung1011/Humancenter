from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlmodel import create_engine, Session, SQLModel


app = FastAPI()
templates = Jinja2Templates(directory="templates")


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# 메인 화면
@app.get("/dsinside")
def main(request: Request):
    return templates.TemplateResponse(request, "main.html")
 

# 로그인 화면
@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse(request, "login.html")

@app.get("/soge")
def lsoge(request: Request):
    return templates.TemplateResponse(request, "soge.html")

# 검색 결과 화면
@app.get("/search")
def search(request: Request, keyword: str = ""):
    return templates.TemplateResponse(
        request,
        "search.html",
        {"keyword": keyword}
    )


# 로그인 처리
@app.post("/api/login")
def login_process():
    try:
        pass
    except Exception:
        pass

    return RedirectResponse(
        url="/dsinside",
        status_code=303
    )

# ==================== 리뷰 수정 ====================
# 리뷰 수정 화면
@app.get("/restaurant/update")
def restaurant_update(request: Request):
    return templates.TemplateResponse(request, "update.html")

@app.get("/review/add")
def review_add(request: Request):
    return templates.TemplateResponse(request, "review_add.html")

# 리뷰 목록 화면
@app.get("/review/list")
def review(request: Request):
    return templates.TemplateResponse(request, "review.html")

# 리뷰 목록 화면
@app.get("/review/add")
def review_add(request: Request):
    return templates.TemplateResponse(request, "review_add.html")

# 
# 회원가입 화면
@app.get("/signup")
def sign_up(request: Request):
    return templates.TemplateResponse(request, "sign_up.html")


# 회원가입 처리
@app.post("/api/signup")
def signup_process():
    return RedirectResponse(
        url="/dsinside",
        status_code=303
    )


# ==================== 마이페이지 ====================

@app.get("/mypage")
def mypage(request: Request):
    return templates.TemplateResponse(request, "mypage.html")


# 관리자 페이지
@app.get("/mypage/admin")
def admin(request: Request):
    return templates.TemplateResponse(request, "admin.html")


@app.get("/mypage/posts")
def mypage_posts(request: Request):
    return templates.TemplateResponse(request, "posts.html")


@app.get("/mypage/reviews")
def mypage_reviews(request: Request):
    return templates.TemplateResponse(request, "reviews.html")


# ==================== 게시판 ====================

@app.get("/board")
def board(request: Request):
    return templates.TemplateResponse(request, "board.html")


@app.get("/board/write")
def board_write(request: Request):
    return templates.TemplateResponse(request, "write.html")


# 서버 실행
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )