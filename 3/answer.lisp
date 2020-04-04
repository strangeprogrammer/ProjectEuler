(defun divideit (todiv divisor)
	(cond
		((= todiv 1)
			NIL)
		((= 0 (mod todiv divisor))
			(cons divisor (divideit (/ todiv divisor) 2)))
		(T
			(divideit todiv (+ 1 divisor)))))

(defun divide-it (todiv)
	(divideit todiv 2))

(defun maximum_ (a l)
	(if (null l)
		a
		(maximum_ (max a (car l)) (cdr l))))

(defun maximum (l)
	(if (not (null l))
		(let ((a (car l)))
		(maximum_ a (cdr l)))))

(maximum (divide-it 600851475143))
