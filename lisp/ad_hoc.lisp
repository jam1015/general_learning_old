(cons 1 2)
(+ 1 (- 10 2))
(+ 4 1000)
(in-package :vlime) ; the new line
(symbol-value (find-symbol "*PACKAGE*" "COMMON-LISP"))  ; the new line
(quit)
(fibonacci:generate 10)
(make-instance 'fibonacci:generator)
