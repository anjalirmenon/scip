(define (pas row col)
	(cond ((or (= row col) (= 1 col)) 1)
		(else (+ (pas (- row 1) (- col 1))
			(pas (- row 1) col)))))
