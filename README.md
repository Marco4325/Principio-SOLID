# Principio-SOLID

Para a apresentação dos princípios selecionados, criei uma situação de entrada de caixa de um mercado que estava pensando para melhorar meu projeto de software. ( por ter sido apenas um código para testar alguns conhecimentos, muita parte da implementação estará esquisita ou errada, então irei focar apenas no que se adequa aos princípios)

# Princípio da responsabilidade única

O princípio da responsabilidade única é a praticamente uma tradução direta da propriedade de coesão. A diferença é que a propriedade estabelece relações únicas de forma genelarizada, enquanto o princípio entra em um sentido de projetar para casos futuros, o qual ao invés de pensar "qual a responsabilidade dessa classe?", pensa "por qual motivo eu modificaria essa classe?".

Para meu código, cada arquivo possui responsabilidade própria, o qual é único para mudanças futuras (assim como suas funções e atributos).

Exemplo das classes CashierValidator.py e CashierEntry.py, respectivamente:

----------------------------------------------------------------------
CashierValidator.py
```
import ENUM
import CashierEntry
from ICashierValidator import ICashierValidator

class CashierValidator(ICashierValidator):

    __OUT_OF_STOCK = [ENUM.ITEMS_IDS.COCA_LATA]
    
    def validateEntry(self, entry: CashierEntry) -> ENUM.VALIDATION:
        for ITEM_ID in self.__OUT_OF_STOCK:
            if ITEM_ID == entry.getITEM_ID():
                return ENUM.VALIDATION.NON_VALIDATED
        return ENUM.VALIDATION.VALIDATED

```

----------------------------------------------------------------------
CashierEntry.py
```
import ENUM
from PaymentMethod import PaymentMethod

class CashierEntry:

    def __init__(self, paymentMethod: ENUM.VALID_PAYMENT_METHODS, ITEM_ID: ENUM.ITEMS_IDS, itemQuantity: int):
        self.__paymentMethod = PaymentMethod(paymentMethod)
        self.__ITEM_ID = ITEM_ID
        self.__totalValue = ITEM_ID.value * itemQuantity

    def getITEM_ID(self):
        return self.__ITEM_ID
```

----------------------------------------------------------------------

É possível observar que na classe CashierValidator, sua responsabilidade é validar a entrada, sendo essa a classe CashierEntry. CashierValidator só possui uma única função, a qual válida entrada, e um único atributo, que indica o que está fora de estoque. CashierEntry possui o necessário para guardar o registro da transação, sendo todos inicializados dentro do construtor, e uma função que retorna o ID do Item do registro de entrada, que será posteriormente validado para então ser armazenado.

O problema que ele resolve é justamente manter o código coeso para situações futuras. Se tudo fosse escrito em uma única classe Cashier, por exemplo, poderia causar aglomeração de informações e uso compartilhado de atributos que não deveriam conversar entre si.

# Princípio da Segregação da Interface

Esse princípio anda lado a lado com o anterior: a ideia é que interfaces também devem ser únicas, com a adição de serem específicas para X cliente. Isso ajuda a evitar interfaces generalizadas que mantém métodos os quais serão utilizados por apenas alguns clientes, quando poderiam na realidade ser quebrados em interfaces menores e mais coesas.

No código que implementei, possuo a interface de validação do caixa:

----------------------------------------------------------------------
ICashierValidator.py
```

from abc import ABC, abstractmethod
from CashierEntry import CashierEntry
import ENUM

class ICashierValidator(ABC):

    @abstractmethod
    def validateEntry(self, entry: CashierEntry) -> ENUM.VALIDATION:
        pass

```

----------------------------------------------------------------------

Essa interface foi criada para o CashierManager, que se trata da classe que gerencia as entradas e saídas do caixa (por enquanto só entradas). A ideia é que diferentes caixas podem querer utilizar diferentes implementações de validações de caixa, mas sem dúvidas todos querem ter validações. No caso do CashierValidator foi implementada a validação por estoque, o qual mostrava que a 'Coca-Lata' estava fora de estoque e então não validava:

----------------------------------------------------------------------
CashierValidator.py
```
import ENUM
import CashierEntry
from ICashierValidator import ICashierValidator

class CashierValidator(ICashierValidator):

    __OUT_OF_STOCK = [ENUM.ITEMS_IDS.COCA_LATA]
    
    def validateEntry(self, entry: CashierEntry) -> ENUM.VALIDATION:
        for ITEM_ID in self.__OUT_OF_STOCK:
            if ITEM_ID == entry.getITEM_ID():
                return ENUM.VALIDATION.NON_VALIDATED
        return ENUM.VALIDATION.VALIDATED

```

----------------------------------------------------------------------
(No exemplo apresentado, CashierManager possui 'printEntries()' puramente por motivos de teste, creio que se fosse um caso real, seria errado tê-lo ali. Creio também que CashierManager poderia se tornar uma interface, já que cada caixa pode querer gerenciar entradas e saídas e sua própria maneira)
CashierManager.py
```

import ENUM
from ICashierValidator import ICashierValidator
from CashierEntry import CashierEntry

class CashierManager:

    def __init__(self, validator: ICashierValidator):
        self.__ENTRIES = []
        self.__CashierValidator = validator

    def addEntry(self, paymentMethod: ENUM.VALID_PAYMENT_METHODS, ITEM_ID: ENUM.ITEMS_IDS, itemQuantity: int):
        newEntry = CashierEntry(paymentMethod, ITEM_ID, itemQuantity)
        validation = self.__CashierValidator.validateEntry(newEntry)
        if validation.value:
            self.__ENTRIES.append(newEntry)

    def printEntries(self):
        for entry in self.__ENTRIES:
            print(entry.getITEM_ID())

```

----------------------------------------------------------------------

Ao testar na classe main:

----------------------------------------------------------------------
main.py
```

import ENUM
from CashierManager import CashierManager
from CashierValidator import CashierValidator

CaixaMercado1 = CashierManager(CashierValidator())

CaixaMercado1.addEntry(ENUM.VALID_PAYMENT_METHODS.PIX, ENUM.ITEMS_IDS.COCA_LATA, 2)
CaixaMercado1.addEntry(ENUM.VALID_PAYMENT_METHODS.CREDITO, ENUM.ITEMS_IDS.MAIONESE, 1)

CaixaMercado1.printEntries()

```

----------------------------------------------------------------------

Saída:
ITEMS_IDS.MAIONESE

----------------------------------------------------------------------

O princípio resolve o problema de eu possuir, por exemplo, uma interface Validator, que faria validação de diversas classes. Porém, como diversas classes variam em suas necessidades, após um tempo a interface Validator se tornaria extremamente grande, porém com cada implementação utilizando apenas uma pequena porção do código, inutilizando boa parte da interface. Então, separando para interfaces menores e mais específicas, criamos implementações coesas.

# Princípio da inversão da dependência

Lado a lado com o princípio anterior, porém dessa vez voltado ao acoplamento, o princípio da inversão de dependência nos permite gerar acomplamentos aceitáveis que não geram uma dependência estrita de uma única classe. Isso permite extensbilidade ao código, além de um acoplamento considerado aceitável ao invés de ruim.

O código implementa isso a partir da classe CashierManager, seguindo a mesma ideia explicada anteriormente: cada caixa pode querer implementar uma validação de forma diferente.

Como foi mostrado anteriormente o código, não colocarei novamente.

A ideia é que como cada interface é implementado de forma única, não existe uma implementação direta de uma classe de validação dentro de CashierManager, sanando o problema que mudanças na classe implementada poderiam afetar a classe de origem, além de resolver o problema de diversos caixas usarem diversas implementações de validação.

# Demeter 

O princípio afirma que métodos não devem ter diversas camadas de chamada para chegarem onde precisam. O problema é que quando essa corrente ocorre, propriedades e princípios são quebrados, como alto acoplamento (que gera muita dependência de um método/classe, sendo afetado por mundanças futuras que não são do seu escopo) e quebra de responsabilidade única, já que pode utilizar de métodos que não deveriam ser de sua responsabilidade.

Novamente, como o código já foi demonstrado, não irei replicá-lo. Porém, observando o código que coloquei, é notório que cada instância ou método chama no máximo um outro método.

Assim como dito anteriormente, isso melhora a coesão do código e abaixa seu acoplamento, criando um código muito mais conciso, agradável, legível e ótimo para modificações.
