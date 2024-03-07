# eq_solver

### Sympy ir vajadzīgs, lai strādātu!
Projekta mērķis ir izveidot funkciju, kura var aprēķināt jebkuru lielumu no lietotāja piedāvātas formulas un izvadīt gan algebrisko, gan skaitlisko atbildi.
Šobrīd funkcija, kas tiek izmantota lai aprēķinātu nepieciešamo vērtību (line 19 - line 54) ir pārāk gara, lai to varētu izmantot vēl citās formulās, tāpēc mēģinu atrast veidu, kā, mainīgo vietā ievietojot lietotāja izvēlētas vērtības, varētu aprēķināt jebkuru formulu. To ir iespējams izdarīt, izmantojot Sympy funkciju 'subs', kas mainīgā vietā ievieto vērtību un aprēķina rezultātu. Kods funkcijai:
```py
form = formula[0].atoms(Symbol, NumberSymbol)
values = {} 
for i in form:
    values[i] = input(f'Enter the value of {i}:')
    print(f'Value of {i} = {values[i]}')
    res = formula.subs({i}, float(values[i]))
    print(res)
```

Problēma funkcijā ir tāda, ka 'subs' strādā tikai ar 'class sympy.core.add.Add' tipa mainīgajiem, taču formula ir 'list' tipa mainīgais un nevaru atrast veidu, kā pārveidot 'list' uz 'class sympy.core.add.Add'.
Pašlaik ievietotā funkcija strādā, taču to nebūtu vēlams darīt katrai pieejamajai formulai, bet ar šeit minēto funkciju būtu iespējams vienkāršā veidā jebkuru formulu aprēķināt.

Darba plāns līdz 4.aprīlim:
Salabot iepriekšminēto funkciju. ;
Programmas sākumā pie iespējamajām funkcijām pievienot vēl citas funkcijas;
Nedaudz izmainīt kodu, lai tas būtu vieglāk lasāms, sadalot programmu 2 funkcijās : mainīgā iznešana no formulas un vērtības aprēķināšana;
Uzzināt vairāk par GUI.
Izstrādāt dizainu, lai lietotājam būtu vieglāk to saprast un izmantot, piemēram, iespējamās formulas pārveidojot par pogām vai drop-down listu, to pašu izdarīt arī ar iespējamjiem mainīgajiem. Visticamāk, lai programma piedāvātu tikai mainīgos, kas ir atrodami lietotāja izvēlētajā formulā, būs nepieciešams izmainīt kodu.































