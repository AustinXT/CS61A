(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  (if (= y 1) x
      (if (even? y)
          (square (pow x (/ y 2)))
          (* x (square (pow x (floor (/ y 2)))))
      )
  )
)