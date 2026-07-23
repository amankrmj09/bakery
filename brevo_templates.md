# Brevo HTML Email Templates for Blu's Bakery

Here are the beautiful, responsive HTML templates for all 11 notification events in Blu's Bakery. The templates use Brevo's default Handlebars syntax (`{{ params.variableName }}`) to inject dynamic data.

### Global Design Notes
- **Colors:** A soft bakery-inspired palette (cream background `#fdfbf7`, deep blue primary `#1e3a8a`, warm accents).
- **Typography:** Clean sans-serif fonts for high readability on all devices.
- **Responsive:** Fluid tables with max-widths to render correctly on mobile and desktop email clients.

---

## 1. User Registration (Welcome)
**Subject:** Welcome to Blu's Bakery
**Params Used:** `firstName`, `lastName`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Blu's Bakery</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #fdfbf7; padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); overflow: hidden;">
                    <tr>
                        <td align="center" style="background-color: #1e3a8a; padding: 30px 20px;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 28px; font-weight: bold; letter-spacing: 1px;">Blu's Bakery</h1>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <h2 style="color: #1e3a8a; margin-top: 0;">Welcome, {{ params.firstName }} {{ params.lastName }}!</h2>
                            <p>We are thrilled to have you join the Blu's Bakery family. Get ready to experience the finest, freshly baked goods delivered right to your door.</p>
                            <p>Whether you're craving a morning croissant, a celebration cake, or just a sweet treat to brighten your day, we've got you covered.</p>
                            <div style="text-align: center; margin: 30px 0;">
                                <a href="#" style="background-color: #f59e0b; color: #ffffff; padding: 14px 28px; text-decoration: none; border-radius: 4px; font-weight: bold; display: inline-block;">Explore Our Menu</a>
                            </div>
                            <p>Stay sweet,<br><strong>The Blu's Bakery Team</strong></p>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="background-color: #f3f4f6; padding: 20px; font-size: 12px; color: #6b7280;">
                            <p style="margin: 0;">© 2026 Blu's Bakery. All rights reserved.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 2. Password Changed
**Subject:** Security Alert - Password Changed
**Params Used:** `firstName`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Security Alert - Password Changed</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; border-top: 5px solid #1e3a8a; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <h2 style="color: #1e3a8a; margin-top: 0;">Password Successfully Changed</h2>
                            <p>Hi {{ params.firstName }},</p>
                            <p>This is a quick notification to let you know that the password for your Blu's Bakery account was recently changed.</p>
                            <p style="background-color: #fef3c7; border-left: 4px solid #f59e0b; padding: 15px; color: #92400e;">
                                <strong>Didn't make this change?</strong><br>
                                Please contact our support team immediately to secure your account.
                            </p>
                            <p>Thanks,<br><strong>Blu's Bakery Security Team</strong></p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 3. OTP Requested
**Subject:** Your OTP Code
**Params Used:** `firstName`, `otpCode`, `expiryMinutes`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Your OTP Code</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); text-align: center;">
                    <tr>
                        <td style="padding: 40px 30px;">
                            <h1 style="color: #1e3a8a; margin-top: 0; font-size: 24px;">Verification Code</h1>
                            <p style="font-size: 16px; color: #4b5563;">Hi {{ params.firstName }},</p>
                            <p style="font-size: 16px; color: #4b5563;">Please use the verification code below to complete your sign-in process.</p>
                            <div style="margin: 30px 0;">
                                <span style="font-size: 36px; font-weight: bold; letter-spacing: 5px; color: #1e3a8a; background-color: #eff6ff; padding: 15px 30px; border-radius: 6px; border: 1px dashed #bfdbfe;">
                                    {{ params.otpCode }}
                                </span>
                            </div>
                            <p style="font-size: 14px; color: #ef4444;">This code will expire in {{ params.expiryMinutes }} minutes.</p>
                            <p style="font-size: 14px; color: #9ca3af; margin-top: 30px;">If you didn't request this code, you can safely ignore this email.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 4. New Sign-In Detected
**Subject:** New Sign-In Detected
**Params Used:** `firstName`, `ipAddress`, `location`, `time`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>New Sign-In Detected</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; border-top: 5px solid #1e3a8a; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <h2 style="color: #1e3a8a; margin-top: 0;">New Device Sign-In</h2>
                            <p>Hi {{ params.firstName }},</p>
                            <p>We noticed a new sign-in to your Blu's Bakery account from a device we don't recognize.</p>
                            
                            <table width="100%" cellpadding="10" cellspacing="0" border="0" style="background-color: #f9fafb; border-radius: 4px; margin: 20px 0;">
                                <tr>
                                    <td width="30%" style="color: #6b7280; font-size: 14px;"><strong>Time:</strong></td>
                                    <td style="font-size: 14px;">{{ params.time }}</td>
                                </tr>
                                <tr>
                                    <td style="color: #6b7280; font-size: 14px;"><strong>IP Address:</strong></td>
                                    <td style="font-size: 14px;">{{ params.ipAddress }}</td>
                                </tr>
                                <tr>
                                    <td style="color: #6b7280; font-size: 14px;"><strong>Location:</strong></td>
                                    <td style="font-size: 14px;">{{ params.location }}</td>
                                </tr>
                            </table>

                            <p>If this was you, you can safely ignore this email.</p>
                            <p style="color: #ef4444; font-weight: bold;">If you don't recognize this activity, please change your password immediately.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 5. Order Confirmed
**Subject:** Order Confirmed!
**Params Used:** `firstName`, `orderId`, `orderNumber`, `totalAmount`, `status`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Order Confirmed</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <tr>
                        <td align="center" style="background-color: #10b981; padding: 40px 20px;">
                            <img src="https://img.icons8.com/ios-filled/50/ffffff/checked--v1.png" width="50" height="50" style="display: block; margin-bottom: 15px;" alt="Checkmark"/>
                            <h1 style="color: #ffffff; margin: 0; font-size: 28px;">We've Got Your Order!</h1>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <p>Hi {{ params.firstName }},</p>
                            <p>Great news! Your order <strong>#{{ params.orderNumber }}</strong> has been confirmed. Our bakers are warming up the ovens and getting everything ready for you.</p>
                            
                            <table width="100%" cellpadding="15" cellspacing="0" border="0" style="border: 1px solid #e5e7eb; border-radius: 6px; margin: 25px 0;">
                                <tr>
                                    <td style="border-bottom: 1px solid #e5e7eb;">
                                        <span style="color: #6b7280; font-size: 12px; text-transform: uppercase;">Order Total</span><br>
                                        <strong style="font-size: 18px;">${{ params.totalAmount }}</strong>
                                    </td>
                                    <td style="border-bottom: 1px solid #e5e7eb;">
                                        <span style="color: #6b7280; font-size: 12px; text-transform: uppercase;">Status</span><br>
                                        <strong style="font-size: 18px; color: #1e3a8a;">{{ params.status }}</strong>
                                    </td>
                                </tr>
                            </table>

                            <p>We'll notify you as soon as your treats are on the way. Thank you for choosing Blu's Bakery!</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 6. Invoice Generated
**Subject:** Your Invoice is Ready
**Params Used:** `firstName`, `orderId`, `orderNumber`, `totalAmount`, `status`, `invoiceUrl`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Your Invoice is Ready</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; border-top: 5px solid #1e3a8a; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <h2 style="color: #1e3a8a; margin-top: 0;">Your Invoice for Order #{{ params.orderNumber }}</h2>
                            <p>Hi {{ params.firstName }},</p>
                            <p>Your invoice has been successfully generated for your recent purchase at Blu's Bakery.</p>
                            
                            <table width="100%" cellpadding="10" cellspacing="0" border="0" style="background-color: #f9fafb; margin: 20px 0;">
                                <tr>
                                    <td width="50%"><strong>Order Number:</strong></td>
                                    <td>{{ params.orderNumber }}</td>
                                </tr>
                                <tr>
                                    <td><strong>Total Amount:</strong></td>
                                    <td>${{ params.totalAmount }}</td>
                                </tr>
                                <tr>
                                    <td><strong>Status:</strong></td>
                                    <td>{{ params.status }}</td>
                                </tr>
                            </table>

                            <div style="text-align: center; margin: 35px 0;">
                                <a href="{{ params.invoiceUrl }}" style="background-color: #1e3a8a; color: #ffffff; padding: 12px 25px; text-decoration: none; border-radius: 4px; font-weight: bold;">Download PDF Invoice</a>
                            </div>

                            <p>Thank you for your business!</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 7. Order Delivered
**Subject:** Order Delivered
**Params Used:** `firstName`, `orderId`, `orderNumber`, `totalAmount`, `status`, `deliveryAddress`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Order Delivered</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; border-top: 5px solid #10b981; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <h2 style="color: #10b981; margin-top: 0;">Enjoy Your Treats!</h2>
                            <p>Hi {{ params.firstName }},</p>
                            <p>Good news! Your Blu's Bakery order <strong>#{{ params.orderNumber }}</strong> has been successfully delivered.</p>
                            
                            <div style="background-color: #f9fafb; padding: 20px; border-radius: 6px; margin: 25px 0;">
                                <p style="margin: 0; color: #6b7280; font-size: 12px; text-transform: uppercase;">Delivered To:</p>
                                <p style="margin: 5px 0 0 0; font-weight: bold;">{{ params.deliveryAddress }}</p>
                            </div>

                            <p>We hope everything is perfectly sweet! If you have any issues with your order, please don't hesitate to contact our support team.</p>
                            <p>Bon Appétit,<br><strong>Blu's Bakery Delivery Team</strong></p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 8. Payment Success
**Subject:** Payment Success
**Params Used:** `firstName`, `orderId`, `paymentId`, `amount`, `status`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Payment Success</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <tr>
                        <td align="center" style="background-color: #1e3a8a; padding: 30px 20px;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 24px;">Payment Receipt</h1>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <p>Hi {{ params.firstName }},</p>
                            <p>Thank you! Your payment was successfully processed. Below are the details of your transaction.</p>
                            
                            <table width="100%" cellpadding="12" cellspacing="0" border="0" style="border-top: 2px solid #f3f4f6; border-bottom: 2px solid #f3f4f6; margin: 25px 0;">
                                <tr>
                                    <td width="50%" style="color: #6b7280;">Amount Paid</td>
                                    <td align="right" style="font-weight: bold; font-size: 18px;">${{ params.amount }}</td>
                                </tr>
                                <tr>
                                    <td style="color: #6b7280;">Transaction ID</td>
                                    <td align="right" style="font-family: monospace;">{{ params.paymentId }}</td>
                                </tr>
                                <tr>
                                    <td style="color: #6b7280;">Status</td>
                                    <td align="right" style="color: #10b981; font-weight: bold;">{{ params.status }}</td>
                                </tr>
                            </table>
                            <p>If you have any questions regarding this transaction, please reply to this email.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 9. Refund Processed
**Subject:** Refund Processed
**Params Used:** `firstName`, `orderId`, `paymentId`, `refundAmount`, `refundReason`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Refund Processed</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; border-top: 5px solid #f59e0b; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <h2 style="color: #d97706; margin-top: 0;">Your Refund is on the Way</h2>
                            <p>Hi {{ params.firstName }},</p>
                            <p>We have processed a refund for your recent transaction (ID: {{ params.paymentId }}).</p>
                            
                            <table width="100%" cellpadding="10" cellspacing="0" border="0" style="background-color: #fef3c7; border-radius: 4px; margin: 20px 0; color: #92400e;">
                                <tr>
                                    <td width="40%"><strong>Refund Amount:</strong></td>
                                    <td style="font-size: 18px; font-weight: bold;">${{ params.refundAmount }}</td>
                                </tr>
                                <tr>
                                    <td><strong>Reason:</strong></td>
                                    <td>{{ params.refundReason }}</td>
                                </tr>
                            </table>

                            <p style="font-size: 14px; color: #6b7280;">Please note that it may take 3-5 business days for the funds to appear back on your original payment method, depending on your bank's processing times.</p>
                            <p>We apologize for any inconvenience. <br><strong>The Blu's Bakery Team</strong></p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 10. Feedback General (Ticket Created)
**Subject:** Feedback Received
**Params Used:** `firstName`, `ticketId`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Feedback Received</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <h2 style="color: #1e3a8a; margin-top: 0;">We hear you!</h2>
                            <p>Hi {{ params.firstName }},</p>
                            <p>Thank you for reaching out to Blu's Bakery. We have successfully received your message.</p>
                            <p>Your support ticket number is: <strong style="color: #1e3a8a;">#{{ params.ticketId }}</strong></p>
                            <p>Our team will review your feedback and get back to you as soon as possible. We strive to provide the best possible experience for our customers, and your input is invaluable to us.</p>
                            <p>Warm regards,<br><strong>Customer Support Team</strong></p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 11. Product Review Thank You
**Subject:** Thank You For Your Review
**Params Used:** `firstName`, `productName`, `rating`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Thank You For Your Review</title>
</head>
<body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); text-align: center;">
                    <tr>
                        <td style="padding: 40px 30px; line-height: 1.6;">
                            <img src="https://img.icons8.com/color/96/000000/star--v1.png" width="60" height="60" style="margin-bottom: 15px;" alt="Star"/>
                            <h2 style="color: #1e3a8a; margin-top: 0;">Thanks for the Review!</h2>
                            <p>Hi {{ params.firstName }},</p>
                            <p>Thank you for taking the time to leave a {{ params.rating }}-star review for our <strong>{{ params.productName }}</strong>.</p>
                            <p>We pour our heart and soul into every bake, and knowing that you enjoyed it absolutely makes our day! Your feedback helps us grow and helps other customers find their new favorite treats.</p>
                            <div style="margin: 35px 0;">
                                <a href="#" style="background-color: #f59e0b; color: #ffffff; padding: 12px 25px; text-decoration: none; border-radius: 4px; font-weight: bold;">Order Again</a>
                            </div>
                            <p>Stay sweet,<br><strong>The Blu's Bakery Team</strong></p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```
