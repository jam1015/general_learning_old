# Local variables

```
(let ((a 5) (b 6)) (+ a b))
```

```
(flet ((function_name (arguments) function boty )
```

Can use do multiple function declarations in `flet`, just wrap each in parens.

## Global Variables And Functions

```
(defparameter *foo* 6)
```

```
(defvar *foo* 7)
```

```
(defun smaller ()
    (setf *big* (1- (guess-my-number)))
    (guess-my-number))
```

`defvar` makes the value permanent

```
( labels  (a (x) (+ x 6))
       (b (x) (+ 6 (a x)))
 (b 10)
)

```

`labels` lets you use the symbols you declare in the delaration		


