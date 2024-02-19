(define (factorial x)
    (if (< x 2) 1
        (* x (factorial (- x 1)))
    )
)

(define (fib n)
    (if (<= n 1) n
        (+ (fib (- n 1)) (fib (- n 2)))
    )
)

(define (my_append a b)
    (if (null? a))
    b
    (cons (car a) (my_append (cdr a) b))

)

(define (duplicate lst)
    (if (null? lst)
    lst
    (cons (car lst) (cons (car lst) duplicate (cdr lst)))
    ))


(define (insert element lst index)
    (if (= index 0)
    (cons element lst) 
    (cons (car lst) (insert element (cdr lst) (- index 1)))
    
    )

)