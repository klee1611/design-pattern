## Factory Method Pattern
### Concept
將**建立目標 object** 的 code 和**使用目標 object** 的完全分離，  
藉此可以更簡單的增加建立目標 object 的 code，   
同時不影響其他的 code。  

也就是可以更簡單的**增加目標 object 的種類**，   
因為可以**輕鬆地為新的種類的 class 建立 constructor**

### Applicability
:paperclip: 當不確定有多少種目標 object 和目標 object 之間的 dependencies 時  
:paperclip: 當希望可以讓使用者能夠輕鬆地擴展 lib 或 framework 中的內部組件時  
