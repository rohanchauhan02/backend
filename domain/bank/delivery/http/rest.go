package http

import (
	"github.com/labstack/echo"
	"github.com/rohanchauhan02/loan-service/domain/bank"
)

type handlerBank struct {
	usecase bank.Usecase
}

func NewHandlerBank(e *echo.Echo, usecase bank.Usecase) {
	handler := &handlerBank{
		usecase: usecase,
	}
	e.POST("/bank", handler.CreateBank)
}

func (h *handlerBank) CreateBank(c echo.Context) error {
	return nil
}
