from datetime import date, timedelta
from typing import Optional
from enum import Enum
from dateutil.relativedelta import relativedelta

class ExpirationStatus(str, Enum):
  FRESH = "fresh"
  EXPIRING_SOON = "expiring_soon"
  EXPIRED = "expired"

"""
Returns calculated expiration date.
Prefers opened_date. Falls back to purchase_date.
Returns None if neither exists
"""
def calculate_expiration_date(
    opened_date: Optional[date], 
    purchase_date: Optional[date],
    expiration_months: int
) -> Optional[date]:
  base_date = opened_date or purchase_date

  if not base_date:
    return None
  
  return base_date + relativedelta(months=expiration_months)

"Determines whether product is fresh, expiring soon, or expired"
def calculate_expiration_status(
    expiration_date: Optional[date],
    warning_window_days: int = 30
) -> Optional[ExpirationStatus]:
  if not expiration_date:
    return None
  
  today = date.today()

  if expiration_date < today:
    return ExpirationStatus.EXPIRED
  
  if expiration_date <= today + timedelta(days=warning_window_days):
    return ExpirationStatus.EXPIRING_SOON
  
  return ExpirationStatus.FRESH

def evaluate_product_expiration(
    opened_date: Optional[date],
    purchase_date: Optional[date],
    expiration_months: int
):
  expiration_date = calculate_expiration_date(
    opened_date,
    purchase_date,
    expiration_months
  )

  status = calculate_expiration_status(expiration_date)

  return {
    "expiration_date": expiration_date,
    "status": status
  }