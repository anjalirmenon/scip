(define (inc n) (+ n 1))
(define (cube x) (* x x x))
(define (sum-cube a b)
	(sum cube a inc b))
