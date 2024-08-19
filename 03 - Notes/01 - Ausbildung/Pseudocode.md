---
Erstellt am: Sonntag, 📅18. August 2024, 🕐17:33:57
Geändert am: Montag, 📅19. August 2024, 🕐15:59:41
tags: [ausbildung/diagramme]
sticker: ""
cssclasses: [wide-callout]
---

# Pseudocode Cheat Sheet

> [!summary] Zusammenfassung
> - **Zweck**: Pseudocode ist ein Mittel, um Algorithmen und Programmabläufe in einfacher, menschenlesbarer Sprache zu beschreiben.
> - **Syntax**: Nutze einfache Begriffe wie `if`, `else`, `for`, `while`, `function` und achte auf logische Einrückung.
> - **Einrückung**: Strukturiere den Code durch konsequente Einrückung, um die logische Hierarchie darzustellen.
> - **Kommentare**: Kommentiere deinen Pseudocode für bessere Verständlichkeit mit `//` oder `#`.
> - **Funktionen und Prozeduren**: Verwende `function` und `procedure` zur Modularisierung des Codes.
> - **Schleifen und Bedingungen**: Nutze `for`, `while`, `if`, `else` zur Steuerung des Programmablaufs.

> [!multi-column]
> 
> > [!error] Version 1
> > - Input card number
> > - Repeat
> > 	- Input pin
> > 	- Check if pin is correct
> > 		- If it’s not output “Wrong pin”
> > - Until the pin is correct
> > - Input amount
> > - If there are enough funds  
> > 	- Dispense cash
> > 	- Update customer’s balance
> > - If there are not enough funds
> > - Output “Sorry, insufficient
> 
> > [!warning] Version 2
> > 
> > ```
> > BEGIN
> >    INPUT CardNumber
> >    REPEAT
> >       INPUT PIN
> >       IF PIN is wrong for this CardNumber THEN
> >          OUTPUT “Wrong PIN”
> >       END IF
> >    UNTIL PIN is correct
> >    INPUT Amount
> >    IF there are enough funds THEN
> >       Dispense Cash
> >       Update customer’s balance
> >    ELSE
> >       OUTPUT “Sorry, insufficient funds”
> >    END IF
> > END
> > ```
> 
> > [!check] Version 3
> > 
> > ```
> > BEGIN
> >    CardNumber=INPUT(“Please enter Card Number”)
> >    DO
> >       Pin=INPUT(“Please enter Pin”)
> >       IF Pin != CorrectPin
> >          PRINT(“Wrong PIN”)
> >       END IF
> >    UNTIL Pin==CorrectPin
> >    Amount=INPUT(“How much money would you like?”)
> >    IF Amount <= CurrentBalence THEN
> >       DispenseCash(Amount)
> >       CurrentBalence = CurrentBalence - Amount
> >    ELSE
> >       PRINT(“Sorry, insufficient funds”)
> >    END IF
> > END
> > ```

> [!multi-column]
> 
> > [!blank]
> > This is too much like structured English.
> > It would receive **little to no credit in an exam**.
> 
> > [!blank]
> > This version is **good**.
> > It uses key words, correct indentation and the logic of the problem can be clearly seen.
> > This would get **decent marks** in an exam.
> 
> > [!blank]
> > This is the **best version**.
> > Mathematical comparison operators used.
> > Variable assignment shown.
> > Complete understanding of the problem to be coded.
> > This would get **full marks in an exam**.

## Beispiel

```markdown title="Finde die Summe und das Maximum in einer Liste"
// Funktion zur Berechnung der Summe einer Liste
function berechneSumme(liste)
    summe = 0
    for i = 1 to length(liste)
        summe = summe + liste[i]
    end for
    return summe
end function

// Funktion zur Bestimmung des Maximums einer Liste
function findeMaximum(liste)
    max = liste[1]
    for i = 2 to length(liste)
        if liste[i] > max
            max = liste[i]
        end if
    end for
    return max
end function

// Hauptprogramm
liste = [3, 7, 1, 9, 5]
summe = berechneSumme(liste)
maximum = findeMaximum(liste)

print("Summe:", summe)
print("Maximum:", maximum)
```