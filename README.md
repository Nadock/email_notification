# Email Notification

Send yourself an email via Gmail's SMTP server, then trigger an iOS Shortcut to push a notification to you.

## Example

```console
python3 ./email_notification.py --to "your.email@example.com" \
                                --from "from.email@example.com" \
                                --subject "Automated Notification Email"
                                --body "Hello, this email is an automated message."
                                --smtp-user your.account@gmail.com
```

```console
"""
From:         from.email@example.com
To:           your.email@example.com
Subject:      Automated Notification Email
Content-Type: text/plain

Hello, this email is an automated message.
"""

📧 Email send successfully, delivery may take a few minutes.
```

## Setup

### Gmail

1. You will need a Gmail account, or some other way to send emails directly via SMTP.
2. If you have 2FA enabled on your Gmail account, you will need an application password. Follow [Google's guide here](https://support.google.com/a/answer/176600?hl=en&fl=1&sjid=16353985817184141519-NC) to generate one.
3. Make a file called `smtp_password.txt` in the repo directory and put your Gmail account or application password in that file.
4. You may also want to [setup an email filter](https://support.google.com/mail/answer/6579?hl=en), but if you do be sure it is still delivered to your inbox.

#### Self-Sending Additional Setup

If you intend to send and receive these emails in the same account, you will need to configure an alias in the Gmail settings and be sure to use that as your `--from` email address. If you don't do this, the email will auto-skip your inbox and will never trigger the iOS shortcut. Follow [Google's guide here](https://support.google.com/mail/answer/22370?hl=en) to set this up, this will only work after the alias is successfully verified.

### iOS Shortcut

1. Open the iOS Shortcuts app on your iPhone, iPad, MacBook, etc.
2. Navigate to the **Automation** tab and tap the **+** to add a new automation.
3. Scroll down to select the **Email** trigger. Then, set the **Sender** field to the address you will use to send from and set the **Account** field to the account you will receive the email in.
   1. Be sure to also set the automation to **Run Immediately**, otherwise you will have to open your iPhone every time.
4. Tap **Next**, the select **New Blank Shortcut** and add the **Show notification** action.
5. Set the input of the **Show notification** action to the shortcut input.
6. Tap **Done** to save the shortcut.
