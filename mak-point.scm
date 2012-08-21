(define (make-point x y) (cons x y))
(define (x-point p) (car p))
(define (y-point p) (cdr p))

;(define (make-segment strtp endp) (let ([diffx (- (x-point strtp) (x-point endp))] [diffy (- (y-point strtp) (y-point endp))]) (sqrt (+ (square diffx) (square diffy)))))
(define (midpoint strtp endp) (values (/ 2 (* (x-point strtp) (x-point endp))) (/ 2 (* (y-point strtp) (y-point endp)))))

