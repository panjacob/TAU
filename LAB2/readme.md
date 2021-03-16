**Testowane strony:**<br/>

- zalando.pl

1) test_login_succesful() <br/>
   1.1) Użytkownik klika ikonkę logowania <br/>
   1.2) Wpisuje poprawny e-mail - testowanie@123.pl <br/>
   1.3) Wpisuje poprawne hasło - qwerty123 <br/>
   1.4) Użytkownik jest zalogowany - Tekst powitalny Witaj Test
2) test_wrong_email() <br/>
   1.1) Użytkownik klika ikonkę logowania <br/>
   1.2) Wpisuje niepoprawny e-mail - @wrongemail.{pl} <br/>
   1.3) Wpisuje poprawne hasło - qwerty123 <br/>
   1.4) Użytkownik otrzymuje informację - "Podaj pełny adres e-mail"
3) test_no_email() <br/>
   1.1) Użytkownik klika ikonkę logowania <br/>
   1.2) Wpisuje niepoprawny e-mail - [puste pole] <br/>
   1.3) Wpisuje poprawne hasło - qwerty123 <br/>
   1.4) Użytkownik otrzymuje informację - "Pole obowiązkowe"
4) test_no_password() <br/>
   1.1) Użytkownik klika ikonkę logowania <br/>
   1.2) Wpisuje poprawny e-mail - testowanie@123.pl <br/>
   1.3) Wpisuje niepoprawne hasło - [puste pole] <br/>
   1.4) Użytkownik otrzymuje informację - "Pole obowiązkowe"

- plemiona.pl

1) test_login_succesful() <br/>
   1.1) Wpisuje poprawną nazwę użytkownika - testowanietest123 <br/>
   1.2) Wpisuje poprawne hasło - qwerty123 <br/>
   1.3) Użytkownik jest zalogowany - Tekst powitalny:  Witaj Testowanietest123
2) test_wrong_username() <br/>
   1.1) Wpisuje niepoprawną nazwę użytkownika - @wrongemail.{pl} <br/>
   1.2) Wpisuje poprawne hasło - qwerty123 <br/>
   1.3) Użytkownik otrzymuje informację: "Konto nie istnieje"
3) test_no_username() <br/>
   1.1) Wpisuje niepoprawną nazwę użytkownika -  [puste pole] <br/>
   1.2) Wpisuje poprawne hasło - qwerty123 <br/>
   1.3) Użytkownik otrzymuje informację: "Konto nie istnieje"
4) test_no_password() <br/>
   1.1) Wpisuje poprawną nazwę użytkownika - testowanietest123 <br/>
   1.2) Wpisuje niepoprawne hasło - [puste pole] <br/>
   1.3) Użytkownik otrzymuje informację: "Konto nie istnieje"