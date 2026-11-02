% Ex 2a - Introduction to PROLOG
% Load in SWI-Prolog:  ?- [ex2a_prolog].

% ---- (i) Minimum and maximum of two numbers ----
minimum(X, Y, X) :- X =< Y.
minimum(X, Y, Y) :- X > Y.
maximum(X, Y, X) :- X >= Y.
maximum(X, Y, Y) :- X < Y.
% ?- minimum(5, 10, Min).            Min = 5.
% ?- maximum(5, 10, Max).            Max = 10.
% ?- minimum(8,3,Min), maximum(8,3,Max).   Min = 3, Max = 8.

% ---- (ii) likes/2 ----
% Base facts are kept in fact/2 so the derived rules cannot loop forever.
fact(mary, food).
fact(mary, wine).
fact(john, wine).
fact(john, mary).

likes(X, Y) :- fact(X, Y).
likes(john, X) :- fact(mary, X).   % 1. John likes anything Mary likes
likes(john, Y) :- fact(Y, wine).   % 2. John likes anyone who likes wine
likes(john, Y) :- fact(Y, Y).      % 3. John likes anyone who likes themselves

% ?- likes(mary, food).    true.
% ?- likes(john, wine).    true.
% ?- likes(john, food).    true.   (because Mary likes food)
% ?- likes(john, Y).       Y = wine ; Y = mary ; Y = food ; Y = wine ; Y = mary ; Y = john.

% ================= OUTPUT (expected, SWI-Prolog) =================
% ?- minimum(5, 10, Min).
% Min = 5 .
%
% ?- maximum(5, 10, Max).
% Max = 10 .
%
% ?- minimum(8, 3, Min), maximum(8, 3, Max).
% Min = 3,
% Max = 8 .
%
% ?- likes(mary, food).
% true .
%
% ?- likes(john, wine).
% true .
%
% ?- likes(john, food).
% true .
%
% ?- likes(john, Y).
% Y = wine ;
% Y = mary ;
% Y = food ;
% Y = wine ;
% Y = mary ;
% Y = john.
