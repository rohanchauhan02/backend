package usecase

import "github.com/rohanchauhan02/loan-service/domain/bank"

type usecaseHandler struct {
	repository bank.Repository
}

func NewBankUsecase(repository bank.Repository) bank.Usecase {
	return &usecaseHandler{
		repository: repository,
	}
}

func (u *usecaseHandler) CreateBank() error {
	return nil
}
