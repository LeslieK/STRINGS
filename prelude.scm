; binomial coefficient (m k)
(define binomial (lambda (m k) (/ (! m) (* (! k) (! (- m k))))))


(define string-map
  (lambda (f str)
    (let loop ((i 0))
      (cond
        [(= i (string-length str)) '()]
        [else (cons (f (string-ref str i))
                    (loop (add1 i)))]))))


(define base-str->ls
  (lambda (str)
    (string-map
      (lambda (char)
        (case char
          [(#\A #\a) 'a]
          [(#\T #\t) 't]
          [(#\G #\g) 'g]
          [(#\C #\c) 'c]
          [else (error 'base-str->ls "Unknown base" char)]))
      str)))

(define ls->base-str
  (lambda (ls)
    (list->string
     (map
      (lambda (sym)
        (case sym
          [(a) #\A]
          [(t) #\T]
          [(g) #\G]
          [(c) #\C]
          [else (error 'ls->base-str "Unknown base" sym)]))
      ls))))



(define base-complement
  (lambda (base)
    (case base
      [(t) 'a]
      [(a) 't]
      [(g) 'c]
      [(c) 'g]      
      [else (error 'base-complement "unknown base" base)])))

(define complement
  (lambda (ls)
    (map base-complement ls)))

(define reverse-complement
  (lambda (ls)
    (reverse (map base-complement ls))))
