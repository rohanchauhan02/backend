package models

type Lead struct{
	BussinessName   string `json:"business_name"`
	BussinessGST    string `json:"bussiness_gst"`
	ContactNumber   int    `json:"contatc_number"`
	Provider        string `json:"provider"`
	LoanAmount      int    `json:"loan_amount"`
}

type LoanEnquiryRequest struct {
	BussinessName   string `json:"business_name"`
	BussinessGST    string `json:"bussiness_gst"`
	ContactNumber   int    `json:"contatc_number"`
	Provider        string `json:"provider"`
	LoanAmount      int    `json:"loan_amount"`
}

type BussinessDetail struct{
	BussinessName   string `json:"business_name"`
	BussinessGST    string `json:"bussiness_gst"`
}

type BalanceSheet struct {
	Year         int     `json:"year"`
	Month        int     `json:"month"`
	ProfitOrLoss float64 `json:"profit_or_loss"`
	AssetsValue  float64 `json:"assets_value"`
}

type LoanEnquiryResponse struct {
	Name            string  `json:"name"`
	PreAssessment   float64 `json:"pre_assessment"`
}
