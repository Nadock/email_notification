import argparse
import pathlib
import smtplib
import ssl
import sys


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        "email_notification",
        description="Send a simple text/plain email via an SMTP server.",
        epilog=(
            "To send via GMail's SMTP server, follow option 2 under described here:\n"
            "https://support.google.com/a/answer/176600?hl=en&fl=1&sjid=16353985817184141519-NC"
        ),
    )

    parser.add_argument(
        "-t",
        "--to",
        required=True,
        nargs="+",
        help=(
            "The address or addresses to send the email to. Can be supplied multiple "
            "times to send to multiple addresses."
        ),
    )
    parser.add_argument(
        "-f",
        "--from",
        required=True,
        dest="_from",
        metavar="FROM",
        help="The email address to send from.",
    )
    parser.add_argument(
        "-s",
        "--subject",
        required=True,
        help="The subject line for the email.",
    )
    parser.add_argument(
        "-b",
        "--body",
        required=True,
        help=(
            'The body of the email. The escape sequences "\\n", "\\r", & "\\t" are '
            'replaced with their literal values, ie: "\\n" is replace by a newline '
            "character."
        ),
    )

    parser.add_argument(
        "--smtp-server",
        default="smtp.gmail.com",
        help="The SMTP server hostname. (default: smtp.google.com)",
    )
    parser.add_argument(
        "--smtp-port",
        type=int,
        default=465,
        help="The SMTP server port number. (default: 465)",
    )
    parser.add_argument(
        "--smtp-user",
        help="The username to login to the SMTP server with. (default: the --from address)",
    )
    parser.add_argument(
        "--smtp-password",
        default="./smtp_password.txt",
        help=(
            "The SMTP server password. If this argument is a path to a file, the "
            "password will be read from that file instead. (default: "
            "./smtp_password.txt)"
        ),
    )
    return parser


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()

    message = [
        f"From:        {args._from}",
        f"To:          {', '.join(args.to)}",
        f"Subject:     {args.subject}",
        "Content-Type: text/plain",
        "",
        args.body.replace("\\n", "\n").replace("\\r", "\r").replace("\\t", "\t"),
    ]
    print('"""', "\n".join(message), '"""', "", sep="\n", file=sys.stderr)

    smtp_user = args.smtp_user or args._from
    smtp_password = args.smtp_password
    path = pathlib.Path(smtp_password)
    if path.is_file():
        smtp_password = path.read_text("utf-8").strip()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(args.smtp_server, args.smtp_port, context=context) as server:
        server.login(smtp_user, smtp_password)
        server.sendmail(args._from, args.to, "\n".join(message))

    print(
        "📧 Email send successfully, delivery may take a few minutes.", file=sys.stderr
    )


if __name__ == "__main__":
    main()
