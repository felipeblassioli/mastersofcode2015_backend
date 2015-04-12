# Create InvoiceItem
import simplify

simplify.public_key = "sbpb_MjM2NWQ2MmUtZWVmZC00Nzk1LTg2ZDctMzUzMDE0ZjE5YzEz"
simplify.private_key = "3bKNdnkpjOFnTDqZFAz7+ot+SMI5D8TPiIsNda20ySt5YFFQL0ODSXAOkNtXTToq"

# invoiceItem = simplify.InvoiceItem.create({
#     "amount" : "1000",
#     "description" : "Invoice Item1",
#     "invoice" : "[INVOICE ID]",
#     "reference" : "ref111"
# })
# print invoiceItem
import simplify

#simplify.public_key = "YOUR_PUBLIC_API_KEY"
#simplify.private_key = "YOUR_PRIVATE_API_KEY"

# invoice = simplify.Invoice.create({
#     "memo" : "This is a memo",
#     "items" : [
#         {
#             "amount" : "5504",
#             #"tax" : "[TAX ID]",
#             "quantity" : "1"
#         }
#     ],
#     "email" : "felipeblassioli@gmail.com",
#     "name" : "Felipe Blassioli",
#     "suppliedDate" : "2394839384000",
#     "note" : "This is a note",
#     "reference" : "Ref2",
#     "currency" : "USD"
# })
# print invoice

 # Status of the invoice. DRAFT - All newly created invoices are created in DRAFT. To send the invoice you must set the invoice status to OPEN. 
 # OPEN - Invoice has not been processed and can have invoice items added to it. 
 # PAID = Invoice has been paid. UNPAID = Invoice was not paid when the card was processed. System will try up to 5 times to process the card. 
 # CANCELLED - No updates are allow to the invoice if it is in a CANCELLED state.

# invoices = simplify.Invoice.list({"max": 30})
# print invoices


# customer = simplify.Customer.create({
#     "email" : "felipeblassioli@gmail.com",
#     "name" : "felipe blassioli",
#     "reference" : "Ref1"
# })
# print customer

# customers = simplify.Customer.list({"max": 30})
# print customers

USER_ID = 'XX8EKBL4'

customer = simplify.Customer.find(USER_ID)
# customer['card'] = {
#     "expMonth" : "11",
#     "expYear" : "19",
#     "cvc" : "123",
#     "number" : "5105105105105100"
# }
# customer.update()

def make_payment(token_id):
    payment = simplify.Payment.create({
        "amount" : "1000",
        "token" : token_id,
        "description" : "payment description",
        "reference" : "7a6ef6be31",
        "currency" : "USD"
    })
    if payment.paymentStatus == 'APPROVED':
        print "Payment approved"

print 'card is'
print customer['card']
def tokenize(c, number):
    return simplify.CardToken.create(
        {"card":{
            "expMonth": str(c['expMonth']),
            "expYear": str(c['expYear']),
            "number": str(number)
            }
        }
    )

cardToken = tokenize(customer['card'],"5105105105105100")
print cardToken
make_payment(cardToken['id'])