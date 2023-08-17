package http

import (
	"github.com/labstack/echo"
	"github.com/rohanchauhan02/loan-service/domain/bank"
	"github.com/rohanchauhan02/loan-service/shared/middleware"
)

type handlerBank struct {
	usecase bank.Usecase
}

func NewHandlerBank(e *echo.Echo, usecase bank.Usecase) {
	handler := &handlerBank{
		usecase: usecase,
	}
	e.GET("/api/bank", handler.CreateBank, middleware.JWTAuthentication)
}

func (h *handlerBank) CreateBank(c echo.Context) error {
	return nil
}
