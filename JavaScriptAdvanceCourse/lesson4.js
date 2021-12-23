'use strict'
let text = "The 'World Wide Web', as people quaintly \
called the Internet in 1996, was more or less made up of \
text. There was no YouTube. There was no 'Facebook'. There \
was, however, Usenet, a loose and difficult-to-navigate \
assortment of message boards. There is nothing wrong with \
wanting to publish - 'or read' - books that have a wide \
potential audience. But it does generate a certain \
'plodding sameness' of tone and subject matter that \
plagues a lot of contemporary American fiction. Our \
Constitution was made only for a moral and religious \
people. It's wholly inadequate to the government of any other."

const regexp = new RegExp("(\\s|^)'(.+?)'", "g")
text = text.replace(regexp, "$1\"$2\"");
console.log(text);

class FormValidator {
    nameValidation(name) {
        const regexp = new RegExp("^[a-zа-я]+$", 'i');
        return name.match(regexp);
    }
    phoneValidation(phone) {
        const regexp = new RegExp("^\\+7\\(\\d{3}\\)\\d{3}\\-\\d{4}$", 'i');
        return phone.match(regexp);
    }
    emailValidation(email) {
        const regexp = new RegExp("^([a-z0-9_\\.-]+)@([a-z0-9_\\.-]+)\\.([a-z\\.]{2,6})$", 'g');
        return email.match(regexp);
    }

}
class Form {
    constructor(validator) {
        this.highlight = "solid red 2px"
        document.querySelector('body').innerHTML =
            '<form action="#">\
                Name <input type="text" placeholder="your name" name="name_input"><br>\
                Phone <input type="text" placeholder="your phone" name="phone_input"><br>\
                E-mail <input type="text" placeholder="your email" name="email_input"><br>\
                Your message: <br>\
                <textarea name="message_input" id="" cols="30" rows="5" class="userInput"></textarea><br>\
            </form>\
            <input type="submit" value="Submit" name="submit_input">';
        const formBtn = document.querySelector("input[name='submit_input']");
        formBtn.addEventListener('click', () => {
            const nameEl = document.querySelector("input[name='name_input']");
            const phoneEl = document.querySelector("input[name='phone_input']");
            const emailEl = document.querySelector("input[name='email_input']");

            if (validator.nameValidation(nameEl.value) == null) {
                nameEl.style.border = this.highlight;
            } else {
                nameEl.style.border = '';
            }

            if (validator.phoneValidation(phoneEl.value) == null) {
                phoneEl.style.border = this.highlight;
            } else {
                phoneEl.style.border = '';
            }

            if (validator.emailValidation(emailEl.value) == null) {
                emailEl.style.border = this.highlight;
            } else {
                emailEl.style.border = '';
            }
        })
    }
}

const validator = new FormValidator()
const form = new Form(validator);