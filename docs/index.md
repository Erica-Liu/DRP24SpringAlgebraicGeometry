# Sudoku and Algebraic Geometry: A cool application of Gröbner bases

*Stephanie Penner*
*Stella Xiao*

## Project Summary

### Our Goal

We wanted to investigate how we could relate Geometry and Algebra, and what that could look like computationally through the use of a Computer Algebra System. 

### The Theoretical Concepts

[comment]: # (<p style="text-align: center"><img align="" width="300" height="" src="https://hackmd.io/_uploads/B1LaYdUY0.jpg">)

We explored how affine varieties can be used to describe a set of points modeling a geometric object, and how these points can be described by polynomial ideal. We looked at the properties of ideals, Gröbner bases and how they can be used to generate polynomial ideals. 

### Our application: Sudoku puzzles!

[comment]: # (![largepreview](https://hackmd.io/_uploads/S1Zpw_IK0.png))

While reading the paper above, we wanted to know if the methods used in the paper to encode Sudoku puzzles with polynomials to count them could be used to actually solve the puzzles themselves. It turns out that a Gröbner basis can solve them, even in a few different methods! 

## Useful Definitions

The following provides the necessary definitions we used in this project.

### Polynomial

A <span style="color:dodgerblue">**polynomial**</span> in $x_1, ..., x_n$ over a field $k$ is a finite linear combination of monomials: 
$$\begin{align*}
f = \alpha_1 \times x^{\beta_1} + \alpha_2 \times x^{\beta_2} ...\\
= \sum_n\alpha_n \times x^{\beta_n},\
\alpha_n \in  k
\end{align*}$$ where $\beta_i$ is a multi index of the form of an n-tuple over $\mathbb{N}$, and for $\beta_i = (a_1, a_2, ..., a_n)$, with $a_1, ..., a_n \in \mathbb{R}$, we have $x^{\beta_i} = x_1^{a_1}x_2^{a_2}...x_n^{a_n}$

Polynomials are often in the form of polynomial equations, examples being:
- quadratic polynomial $f(x) = 12 + 4x + 7x^2$ for $x$ over the field $\mathbb{R}$
- $f(x, y) = x^2 + y^2$
    <p style="text-align: center"><img align="" width="" height="" src="https://hackmd.io/_uploads/SkcpsH8t0.gif"> 
- $f(x, y) = x^2 - y^2$<p style="text-align: center"><img align="" width="" height="" src="https://hackmd.io/_uploads/r1cTjBIFA.gif">

### Polynomial Ring
A <span style="color:dodgerblue">**Polynomial Ring**</span> in $x_1, ..., x_n$ with coefficients over field $k$ is the set of all formal sums (polynomials) in the form: $\sum_{n} \alpha_n  x^{n}, \space \alpha_n \in k,$ denoted by
\begin{align*}
k[x_1, ..., x_n]
\end{align*}
Some examples of a polynomial ring include $\mathbb{R}[x]$, which contains every equation of the form $a_0+a_1x+a_2x^2+...+a_nx^n$ where $a_0, ..., a_n \in \mathbb{R}$ and $x$ is a variable over $\mathbb{R}$, and $\mathbb{C}[x, y]$ which contains polynomial equations in the variables $x$ and $y$ over the complex numbers, which include $x^2 + y^2 -1$, $x+iy + 4$, and $x^2 + xy + x^2$

    
    
<details>
<summary>Some additional definitions</summary> 

### Zero Locus
	
The <span style="color:dodgerblue">**Zero Locus**</span> of a function $f$ is the set of points such that $f = 0$.
   
For example, the set $\{(x,y) \,|\, x^2 + y^2 = 1\}$ is zero locus of the function $f(x, y) =  x^2 + y^2 -1$. You may be familiar with it as the unit circle.

### Affine Spaces
	
An n-dimensional <span style="color:dodgerblue">**Affine Space**</span> over $k$ is the set
\begin{align*}
k^n = \set{(a_1, \dots, a_n) | a_i \in k}
\end{align*}
	
<br>
</details>

	
### Affine Varieties
Affine varieties are one of the first major new concepts we spent significant time with. Our understanding of varieties was characterized by the idea that they represent a set of points that model some geometric object.

An affine variety is defined as follows:
Given field $k$, and polynomials $f_1, ..., f_s \in k[x_1, ..., x_n]$, the <span style="color:dodgerblue">**Affine Variety**</span> defined by polynomials $f_1, \dots, f_s$ is a subset of $k^n$ where:
\begin{align*}
V(f_1, \dots, f_s) = \set{(a_1, \dots, a_n) \in k^n | f_i(a_1, \dots, a_n) = 0, i=1, \dots, s}
\end{align*}
In other words, the Affine Variety on $f_1, ..., f_n$ is represented by the set of all points in $k^n$ where $f_1(x_1, ..., x_n), ..., f_s(x_1, ..., x_n) = 0.$
#### Examples
Revisiting an earlier example, <span style="color:dodgerblue">the affine variety for the unit circle</span>: $V(x^2+y^2-1)$
<p style="text-align: center"><img align="" width="" height="" src="https://hackmd.io/_uploads/Bk04hSIt0.png">

Visual representation of the affine variety: $V(z^2-y^2-x^2)$
<p style="text-align: center"><img align="" width="" height="" src="https://hackmd.io/_uploads/BJS-wATu0.png">


### Ideals
We spent a significant amount of time working with ideals, working to understand what they represent and how they can be used. 

Formally, and **ideal** is a subset $I \subset k[x_1, ..., x_n]$ such that the followings are true:
1. $0 \in I$
2. $I$ is closed under addition, meaning that if $f, g \in I$ then $f+g \in I$
3. $I$ is closed under multiplication in the general ring the ideal is defined on, meaning $f \in I$ and $h \in k[x_1, ..., x_n]$ then $fh \in I$. 

Intuitively, <span style="color:dodgerblue">a polynomial ideal describes a set of polynomials with a common set of vanishing points (points where the polynomials evaluate to zero). </span>

We will often represent ideals in two ways: 
- We write <span style="color:dodgerblue">$\langle f_1, ..., f_s\rangle$</span> to denote the ideal that is generated by $f_1, ..., f_s$. Essentially, $\langle f_1, ..., f_s\rangle$ is the set of all functions of the form $\sum_{i = 1}^s h_if_i$ where $h_i \in k[x_1, ..., x_n]$.
- We write <span style="color:dodgerblue">$I(V)$</span> to denote the set of all the functions that vanish on the points in the variety, $V$.

## The Ideal Membership Problem
Now that we have defined ideals and their properties, let's take a different approach. <span style="color:dodgerblue">Consider $f_1, ..., f_s \in k[x_1, ..., x_n]$, how can we know if $f$ lies in ideal $\langle f_1, ..., f_s \rangle$?</span> Based on the definition, we can check through conditions if given an 'easy' ideal, whether polynomial $f$ is a member or not. Intuitively, we want to find polynomials $h_1, h_2, ..., h_s \in k[x_1, ..., x_n]$ such that:
\begin{align*}
f = f_1h_1 + ... + f_sh_s 
\end{align*}
Let's look at some simple examples:
- Is $x^2 \in \langle x^3\rangle$?
No, since we can't write $x^2$ as $x^3$ multiplied by a polynomial. $\frac{1}{x}$ is not one.

- Is $x^2y + x \in \langle xy + 1 \rangle$?
Yes! 
\begin{align*}
x^2y+x = x(xy+1)
\end{align*}
- <span style="color:dodgerblue">Is $x^2y-y \in \langle x^2 - xy - 1, xy + 1 \rangle$?</span>
Yes!
\begin{align*}
x^2y-y = y(x^2-xy-2) + (xy^2+y)\\
= y(x^2-xy-2) + y(xy+1) + 0\
\end{align*}

Now we have an idea of how to solve the Ideal Membership Problem, you may recognize this as the division algorithm as we did, so let's generalize the algorithm to be applied to every problem.

### Lexicographical Order
Through the examples, it's very apparent that polynomial <span style="color:dodgerblue">$f$ is contained within an Ideal if it is divisible by elements of that Ideal.</span> In other words, the remainder eventually becomes 0 after applying divisions.

A question that arose for us when more variables were involved: 
<span style="color:dodgerblue">**Is the final remainder unique?**</span>

<details>
<summary>More details</summary>
    
We revisited our last example with a different approach, and divided by $xy + 1$ first:
- Is $x^2y-y \in \langle x^2 - xy - 1, xy + 1 \rangle$?
\begin{align*}
x^2y-y = x(xy+1) - x + y\\
\end{align*}

Our remainder this time is $(-x+y)$ instead of $0$, and our conclusion is now also different: $x^2y-y \notin \langle x^2 - xy - 1, xy + 1 \rangle$. This is tricky, which answer is correct? 
<br>
</details>
	
We introduced <span style="color:dodgerblue">**Lexicographical Order**</span>:

Let $\alpha = (\alpha_1, \ldots, \alpha_n)$, $\beta = (\beta_1, \ldots, \beta_n) \in \mathbb{Z}_{\geq 0}^n$. We say $\alpha >_{\text{lex}} \beta$ if the leftmost nonzero entry of the vector difference $\alpha - \beta \in \mathbb{Z}^n$ is positive. 
Denoted $x^\alpha >_{\text{lex}} x^\beta$ if $\alpha >_{\text{lex}} \beta$.

<span style="color:dodgerblue">When working with polynomials we will use $x, y, z...$ and assume that ordering is by alphabetical order unless stated otherwise: $x > y > z$.</span>

Given lexicographic ordering, there is a distinct approach for every ideal membership division problem. We found that when following an ordering, all remainders are unique and therefore all membership problems have unique answers.

Assuming $x > y$ and the first approach, $x^2y-y \in \langle x^2 - xy - 1, xy + 1 \rangle$ is true.

### Division Algorithm
Using Lexicographical ordering, we can describe a division algorithm to divide the polynomial $f \in k[x_1, ..., x_n]$ by a set of polynomials $f_1, ..., f_s$

An <span style="color:dodgerblue">**example**</span> of how this algorithm would work is: divide $f = xy^2 + 1$ by $f_1 = xy+1$ and $f_2 = y+1$.

1. Note that $f_1 >f_2$ by lexicographical order.
2. Long Division:
i)\begin{array}{r}
                y  \\[-3pt]
xy +1 \overline{)xy^2 + 1} \\[-3pt]
     \underline{xy^2+y}\phantom{} \\[-3pt]
                1-y  \\[-3pt]
\end{array}
$f = xy^2 + 1 = y(xy + 1) - y + 1$ 
ii) \begin{array}{r}
	-1\\[-3pt]
                y+1\overline{)-y+1}  \\[-3pt]
     \underline{-y-1}\\
	2  \\[-3pt]
\end{array}	
	$f = xy^2 + 1 = y(xy + 1) - 1(y + 1) + 2$ 
	
3. The result of the division algorithm: We can write $f$ as a product of $f = q_1 f_1 + q_2 f_2 + r,$ for $q_1, q_2, r \in k[x_1, \ldots, x_n]$
	We get that:
	$f = xy^2 + 1 = y(xy + 1) - 1(y + 1) + 2$ 
	for $r = 2$
	


We have that either $r = 0$ or $r$ is a monomial in $k[x_1, ..., x_n]$, with coefficients in $k$, of monomials, none of which is divisible by any of the Leading Terms of the Ideal Generators: $\text{LT}(f_1), \text{LT}(f_2)$. We call $r$ the remainder of $f$ on division.

## Simplifying Polynomial Ideals

To solve the ideal membership problem, we want be able to describe any ideal by some finite generating set, to make it easier to see if a polynomial can be created by this set and is therefore in the ideal. In our readings, we also noticed that <span style="color:dodgerblue">some ideals have multiple representations.</span> For example,\begin{align*} \langle x+xy, y+xy,x^2, y^2\rangle = \langle x,y\rangle \end{align*} and \begin{align*} \langle 2x^2+3y^2-11, x^2-y^2-3 \rangle = \langle x^2-4, y^2-1\rangle \end{align*} Evidently, <span style="color:dodgerblue">$\langle x,y\rangle$ and $\langle x^2-4, y^2-1\rangle$ seem simpler</span> and nicer to work with, but this raised some questions like:
- What does it mean for an ideal to be simplified?
- How can we describe an ideal in terms of generating functions in their simplest form?
- What about ideals that are not defined implicitly as the equations that vanish on the points in a variety?


As it turns out, <span style="color:dodgerblue">most of these questions are answered by what's called a Gröbner basis,</span> which gives us a finite generating set of polynomials for an ideal. Gröbner bases and polynomial division also lead to a neat solution to the ideal membership problem!.

### Our observation

While working with the idea of how we could simplify ideals, we observed the following:

Given an ideal $I \in K[x_1, x_2, ..., x_n]$, and $f_1, f_2, f_3\in I$, <span style="color:dodgerblue">we can reduce the complexity of some ideal generated by $f_1, f_2, f_3$ </span>using the following three steps:

- for $h\in k[x_1, x_2, ..., x_n]$, and $c \in k$, $\langle cf_1 + hf_2, f_2\rangle = \langle f_1, f_2\rangle$
-  $\langle f_1, f_2 \rangle \subseteq \langle f_1, f_2, f_3 \rangle$
-  $f_3 \in \langle f_1, f_2 \rangle$ if and only if $\langle f_1, f_2, f_3 \rangle = \langle f_1, f_2 \rangle$
    

<details>
<summary>Principle Ideal Domain and Dickson's Lemma</summary>
<br>

### Principle Ideal and Principle Ideal Domain (PID)
When working with simplifying one variable ideals over $k[x]$, we found that any ideal $\langle f_1, f_2 \rangle$ can be written as an ideal generated by one element $\langle h \rangle$ where polynomial $h = gcd(f_1, f_2)$. An ideal generated by one element is called a <span style="color:dodgerblue">**principle ideal**</span>. We found that this simplification can be applied to any ideals over $k[x]$ until one element remains.

We can conclude that every ideal over some $k[x]$ can be written as a principle ideal $\langle h \rangle$. Furthermore, we have that $h$ is unique. 

We say that $k[x]$ is a principle ideal domain, abbreviated **PID**.
	
### Monomial Ideals and Dickson's Lemma	

First, a monomial ideal can be thought of as an ideal generated by monomials. 
We denote a monomial ideal as $\langle x^a : a \in A \rangle$, where $A$ is an indexing set. Dickson's lemma:
<span style="color:dodgerblue">*Let $I = \langle x^a : a \in A \rangle \subseteq k[x_1, ..., x_n]$ be a monomial ideal. Then $I$ can be written in the form $I=\langle x^{a_1}, ..., x^{a_s} \rangle$ with $a_1, ..., a_n \in A$*</span>
	
Dickson's lemma answers many of our questions, and shows us that any monomial ideal has a finite generating set of polynomials, or a basis or sorts

We can use Dickson's lemma and polynomial division to expand this idea to polynomial ideals in general.
</details>


### Hilbert Bases Theorem and Gröbner bases

The Hilbert Basis Theorem answers our questions in the more general case, and says the following:
<span style="color:dodgerblue">*Every ideal $I \subset k[x_1, ..., x_n]$ has a finite generating set. That is, $I = \langle g_1, ..., g_t \rangle$ for some $g_1, ..., g_n \in I$*</span>

From Hilbert Basis theorem, we get an idea of a basis for an ideal as the finite generating set of polynomials for ideal, which we now know can be found for any ideal. 

We can expand on this idea to get a more standard notion of a basis for an ideal, called a Gröbner Basis. 

Formally, a <span style="color:dodgerblue">**Gröbner Basis** </span>for an ideal is a subset <span style="color:dodgerblue">$G=\{g_1, ..., g_t\} \subset I$ where $\langle LT(g_1), ..., LT(g_t)\rangle = \langle LT(I)\rangle$</span> where we let $LT(f)$ be the leading term of the polynomial $f$, and where  $\langle LT(I)\rangle$ is the monomial ideal constructed by the leading terms of each the polynomials in $I$. 

Using elements of the proof of Hilbert Basis theorem, we can show that <span style="color:dodgerblue">every ideal $I$ has a Gröbner Basis,</span> and that any <span style="color:dodgerblue">Gröbner Basis is a basis for $I$</span>. 

### How Gröbner Bases Solve the Ideal Membership Problem

Using our new knowledge of Gröbner basis and the division algorithm for polynomials with multiple variables, we have the general solution to the Ideal Membership Problem!

With a fixed ordering on the variables $x_1, ..., x_n$ in $k[x_1, ..., x_n]$, for any ideal $I \subseteq k[x_1, ..., x_n]$ we can find the Gröbner Basis for $I$ (which gives us a nice generating set for our ideal). Then take any polynomial $f \in k[x_1, ..., x_n]$ divide it by the elements of the Gröbner Basis for $I$. <span style="color:dodgerblue">If the remainder is $0$,</span> $f$ can be made from a combination of the basis polynomials that generate $I$, so <span style="color:dodgerblue">$f$ must be in $I$,</span> and otherwise, $f$ is not in $I$, solving the ideal membership problem!


## Application - Sudoku Puzzles!

<figure>
  <p style="text-align: center"><img src="https://hackmd.io/_uploads/Bk7-rGyYC.png" alt="Example sudoku board puzzle">
  <figcaption> This is a Sudoku puzzle that we used as an example to calculate the solution to with Gröbner basis [3].</figcaption>
</figure>

[\\]: # "![sudoku(https://hackmd.io/_uploads/H1cfmCpOC.jpg) - other example of empty board"

A cool application of what we learned is that <span style="color:dodgerblue">given a 9x9 Sudoku puzzle, we could solve it by using a Gröbner Basis!</span> The paper, **"Gröbner Basis Representations of Sudoku"**, talks about representing Shidoku puzzles (4x4 Version of Sudoku) in polynomials, in a few different methods which made us curious of if we could expand these methods to 9x9 Sudoku boards. 
	
We used SageMath, a Computer Algebra System, to compute the Gröbner basis for a system of polynomials that encodes a Sudoku puzzle in math, we could solve the puzzle! Later we take a look at the code and the methods we used to do this.

### Roots of Unity Model

#### The Method

The roots of unity system is one of the methods for encoding a Sudoku puzzle in polynomials that uses roots of unity. The general idea is that we will <span style="color:dodgerblue">map each number from 1 to 9 in the original puzzle to one of the 9th roots of unity</span>, and then will <span style="color:dodgerblue">solve the puzzle in terms of roots of unity</span>, and will then <span style="color:dodgerblue">map our roots of unity back to the numbers 1 to 9</span> to get the solution to our original numbers.

Recall that a 9th root of unity is of the form <span style="color:dodgerblue">$e^{\frac{2x \pi\cdot i}{9}} = \cos (\frac{2\pi x}{9}) + i\cdot \sin(\frac{2\pi x}{9})$</span>, for $x \in \mathbb{Z}$. Representing these roots visually, we have:
<figure>
  <p style="text-align: center"><img src="https://hackmd.io/_uploads/BJVguADYC.png" alt="Roots of unity diagram, around a circle">
</figure> 

The following table illustrates our <span style="color:dodgerblue">bijection between the integers 1 to 9 and the 9th roots of unity</span>, and shows how each root will be represented in SageMath, which will become important later:


| Integers | Roots of Unity                 | Polar Coordinates:                                |SageMath Representation|
| -------- | ------------------------------ | ------------------------------------------------- | --------------------- |
| 1        | $e^{\frac{2\pi i}{9}}$         |$\cos (\frac{2\pi}{9})+i\sin(\frac{2\pi}{9})$|                ```zeta9```|
| 2        | $e^{\frac{2\cdot 2\pi i }{9}}$ |$\cos (\frac{2\cdot 2\pi}{9})+i\sin(\frac{2\cdot 2\pi}{9})$|```zeta9^2```       |
| 3        | $e^{\frac{3\cdot 2\pi i}{9}}$  |$\cos (\frac{3\cdot 2\pi}{9})+i\sin(\frac{3\cdot 2\pi}{9})$|```zeta9^3```      |
| 4        | $e^{\frac{4\cdot 2\pi i}{9}}$  |$\cos (\frac{4\cdot 2\pi}{9})+i\sin(\frac{4\cdot 2\pi}{9})$|```zeta9^4```     |
| 5        | $e^{\frac{5\cdot 2\pi i}{9}}$  |$\cos (\frac{5\cdot 2\pi}{9})+i\sin(\frac{5\cdot 2\pi}{9})$|```zeta9^5```      |
| 6        | $e^{\frac{6\cdot 2\pi i}{9}}$  |$\cos (\frac{6\cdot 2\pi}{9})+i\sin(\frac{6\cdot 2\pi}{9})$|```-zeta9^3 - 1```      |
| 7        | $e^{\frac{7\cdot 2\pi i}{9}}$  |$\cos (\frac{7\cdot 2\pi}{9})+i\sin(\frac{7\cdot 2\pi}{9})$|```-zeta9^4 - zeta9```|
| 8        | $e^{\frac{8\cdot 2\pi i}{9}}$  |$\cos (\frac{8\cdot 2\pi}{9})+i\sin(\frac{8\cdot 2\pi}{9})$|```-zeta9^5 -zeta9^2```|
| 9        | $e^{\frac{9\cdot 2\pi i}{9}}$  |$\cos (\frac{9\cdot 2\pi}{9})+i\sin(\frac{9\cdot 2\pi}{9})$|```1```     |


#### The Equations
Now we will introduce the polynomials that represent our Sudoku puzzle! We want to construct an ideal of the polynomial equations that will represent our Sudoku puzzle. Let's let this ideal be $I$, and consider the following four steps:

1. Suppose <span style="color:dodgerblue">each individual box on the Sudoku board is represented by a variable $x_{ij}$</span> for $1 \leq i,j \leq 9$, where $x_{i,j}$ is represented as the $i, j$ coordinate of the board, which visually looks as follows: <p style="text-align: center"><img src="https://hackmd.io/_uploads/BJV8H0vKR.png" alt="Visual of roots of unity diagram"> <p style="text-align:left">This means that we set up $I$ to be an ideal in a polynomial ring of 81 variables! Since we will be working with roots of unity which are complex, we get <span style="color:dodgerblue">$I \subset \mathbb{C}[x_{1,1}, x_{1,2}, ..., x_{1, 9}, ..., x_{9,1}, x_{9, 2}, ..., x_{9,9}]$</span>

2. First, we want each $x_{ij}$ to represent a number from 1 to 9, which translates to each $x_{ij}$ being equal to some 9th root of unity from our bijection. Then solving for the value of each $x_{ij}$ is equivalent to solving for the numbers to solve our Sudoku board. 
 Translating this into equations, first notice that for any $x\in \mathbb{R}$, we have:
\begin{align*}(e^{\frac{2x \pi\cdot i}{9}})^9 = e^{2x \pi\cdot i}=\cos (2\pi x) + i\cdot \sin(2\pi x) = \begin{cases} 1 & \text{if } x\in \mathbb{Z}\\
\text{not } 1 & \text{otherwise}
\end{cases}
\end{align*} <span style="color:dodgerblue">So, only any 9th root of unity will satisfy the equation $x^9 - 1 = 0$.</span> This means the equations <span style="color:dodgerblue">$x_{ij}^9 - 1 = 0$</span> for $1 \leq i, j \leq 9$ represent restricting each value of our Sudoku board to a 9th root of unity as we want, so let's require all these equations to be in $I$. 

3. Next, we want to add equations that represent the known starting values of our puzzle to our ideal. This is easily done, since the equation <span style="color:dodgerblue">$x-a=0$ represents that $x=a$,</span> so for every $x_{ij}$ that we know as $e^{\frac{2\pi i x}{9}}$ for $x\in \{1,..., 9\}$ of at the start of our puzzle, we require the equation <span style="color:dodgerblue">$x_{ij}-e^{\frac{2\pi i x}{9}}$ </span>to be in $I$. Consider the top-left corner of our Sudoku board: <p style="text-align: center"><img src="https://hackmd.io/_uploads/HJN8SAwFA.png" alt="Visual representation of mapping set values from our puzzle to the equations we want"> <p style="text-align:left">


4. Last, we want to represent the given restrictions for a Sudoku puzzle in polynomial equations that we can add to an ideal. These restrictions are that for a given entry represented by $x_{ij}$, none of the other entries in the puzzle in the same row, column or box will have the same value as $x_{ij}$. Visually this looks like for the variable $x_{24}$, none of the highlighted variables can have the same value as $x_{24}$. <p style="text-align: center"><img src="https://hackmd.io/_uploads/S148BCvKC.png" alt="Visual of roots of unity diagram"> <p style="text-align:left"> Let $x, w \in \{x_{ij}\,|\, 1 \leq i, j \leq 9 \}$, where we don't want $x$ and $w$ to have the same value. Then from the previous step, $x^9-1=0$ and $w^9-1=0$ so\begin{align*} x^9-1&=w^9-1\\ x^9-1-w^9+1&=0\\ x^9 - w^9 &= 0\\ (x-w)(\sum_{i=0}^8 x^iw^{8-i})&=0\end{align*} The root $(x-w)$ in this equation represents the solution where $x=w$, which is exactly what we *don't* want, so the equation <span style="color:dodgerblue">$(\sum_{i=0}^8 x^iw^{8-i})=0$ represents all the solutions where $x\not = w$,</span> so we want to require this equation to be in $I$ for all the pairs variables that we want to be different in our puzzle.
    
Now we have created an ideal, $I$, made of polynomials that encode all the useful information we know about Sudoku puzzle. In theory, since our Sudoku puzzle has a unique solution, <span style="color:dodgerblue">this massive system of equations should give us a unique value for every variable when solved.</span> So, when we calculate the Gröbner basis on $I$, we should get a basis of 81 polynomials that each have the form $x_{ij} - a$, where $a$ is some root of unity. This is because a Gröbner basis has the property that for every $f \in I$, the leading term of $f$ must be divisible by some leading term of something in our Gröbner basis. Since our Ideal represents all polynomials with roots on our solution set, our <span style="color:dodgerblue">Gröbner basis must be made of the roots of the system, meaning equations of the form $x_{ij} - a$.</span> Then we replace each $x_{ij}$ the with number $a$ represents, we get our solved Sudoku board!


#### The Computation
Since the computation for the Gröbner basis would be waaaay to large to do by hand, we used <span style="color:dodgerblue">a Computer Algebra System, SageMath to code and compute our solution.</span>

We put together the code for constructing the set of the equations we want in our ideal in the following four steps, which follow similarly from the steps we took to construct the ideal $I$:
1. We first set up the ring containing the ideal $I$, a matrix ```board``` representation of the variables we were working under for easy access later, as well as the specific Sudoku puzzle we were trying to solve, as follows:
```python 
import itertools
UCF = CyclotomicField(9); UCF
R = UCF['x11, x12, x13, x14, x15, x16, x17, x18, x19, x21, x22, x23, x24, x25, x26, x27, x28, x29, x31, x32, x33, x34, x35, x36, x37, x38, x39, x41, x42, x43, x44, x45, x46, x47, x48, x49, x51, x52, x53, x54, x55, x56, x57, x58, x59, x61, x62, x63, x64, x65, x66, x67, x68, x69, x71, x72, x73, x74, x75, x76, x77, x78, x79, x81, x82, x83, x84, x85, x86, x87, x88, x89, x91, x92, x93, x94, x95, x96, x97, x98, x99']
(x11, x12, x13, x14, x15, x16, x17, x18, x19, 
    x21, x22, x23, x24, x25, x26, x27, x28, x29,
    x31, x32, x33, x34, x35, x36, x37, x38, x39,
    x41, x42, x43, x44, x45, x46, x47, x48, x49,
    x51, x52, x53, x54, x55, x56, x57, x58, x59,
    x61, x62, x63, x64, x65, x66, x67, x68, x69,
    x71, x72, x73, x74, x75, x76, x77, x78, x79,
    x81, x82, x83, x84, x85, x86, x87, x88, x89,
    x91, x92, x93, x94, x95, x96, x97, x98, x99) = R.gens()

board = matrix(R, [[x11, x12, x13, x14, x15, x16, x17, x18, x19], 
                   [x21, x22, x23, x24, x25, x26, x27, x28, x29], 
                   [x31, x32, x33, x34, x35, x36, x37, x38, x39], 
                   [x41, x42, x43, x44, x45, x46, x47, x48, x49], 
                   [x51, x52, x53, x54, x55, x56, x57, x58, x59], 
                   [x61, x62, x63, x64, x65, x66, x67, x68, x69], 
                   [x71, x72, x73, x74, x75, x76, x77, x78, x79], 
                   [x81, x82, x83, x84, x85, x86, x87, x88, x89], 
                   [x91, x92, x93, x94, x95, x96, x97, x98, x99]])

sudoku = [5, 3, 0, 0, 7, 0, 0, 0, 0, 
        6, 0, 0, 1, 9, 5, 0, 0, 0, 
        0, 9, 8, 0, 0, 0, 0, 6, 0, 
        8, 0, 0, 0, 6, 0, 0, 0, 3, 
        4, 0, 0, 8, 0, 3, 0, 0, 1, 
        7, 0, 0, 0, 2, 0, 0, 0, 6, 
        0, 6, 0, 0, 0, 0, 2, 8, 0, 
        0, 0, 0, 4, 1, 9, 0, 0, 5, 
        0, 0, 0, 0, 8, 0, 0, 7, 9]
```
We also set up our bijection between the integers 1 to 9 and the 9th roots of unity as the functions root_to_val and val_to_root, and print our initial board:
```python 
def root_to_val(z):
    val = -1
    for  k in range (9):
        if z == UCF.gen()^k:
            val = k
    if val == 0:
        val = 9
    return val

def val_to_root(x):
    return (UCF.gen())^x 

for r in range(9):
    for c in range(9):
        val = sudoku[r*9+c]
        if val == 0:
            print('-', end=' ')
        else:
            print(val, end=' ')
    print()

```
2. We first create a list ```gens``` to add all the equations representing $I$ to, and then we first add the restrictions of <span style="color:dodgerblue">$x_{ij}^9-1=0$</span> to this set, by looping through all our variables:
```python
gens = []

for row in range (9):
    for col in range (9):
        gens.append(board[row][col]^9-1)
        
```
3. Next, we add the equations that represent the initial values we know of our Sudoku puzzle:
```python
for item in range(81):
    if sudoku[item] != 0:
        gens.append(board[item // 9][item % 9] - val_to_root(sudoku[item]))
```
4. Last, we add the equations that represent restricting variables in the same rows, columns, or boxes to be not equal to each other. Recall these are the equations where for $x, w \in \{x_{ij} | 1 \leq x_{ij} \leq 9 \}$, $x$ and $w$ are not equal, we have <span style="color:dodgerblue">$\sum_{i=0}^8 x^i w^{8-i}$.</span> In SageMath, this looks like:
```python
def constraints(x, y):
    sum = 0
    for k in range(9):
        sum += x^k*y^(8-k)
    return sum
    
for row in board:
    for x, y in itertools.combinations(row, 2):
        gens.append(constraints(x, y))


for col in board.transpose():
    for x, y in itertools.combinations(col, 2):
        gens.append(constraints(x, y))

for row in (0, 3, 6):
    for col in (0, 3, 6):
        for x, y in itertools.combinations(itertools.chain.from_iterable(board.submatrix(row, col, 3, 3)), 2):
            gens.append(constraints(x,y))
           
```
After constructing the set of the equations we want in our ideal, we turned the list ```gens``` into a set, <span style="color:dodgerblue">constructed an ideal $I$ on from our set of generators, and computed the Gröbner basis B on $I$,</span> and printed the results:
```python
X= Set(gens)
print('Number of generators: ' + str(X.cardinality()))

I = R.ideal(list(X))
B = I.groebner_basis()
print(B)

print('Solved sudoku board:')
def print_num_board():
    for r in range(9):
        for c in range(9):
            root = B[r*9+c] - board[r][c]
            val = root_to_val(-root)
            print(val, end=' ')
        print()
    
def print_roots_board():
    for r in range(9):
        for c in range(9):
            root = B[r*9+c]
            print(root, end='   ')
        print()
print('in polynomial equations:')
print_roots_board()
print('in sudoku numbers:')
print_num_board()
```
...And this outputs the solution of our Sudoku puzzle!
![image](https://hackmd.io/_uploads/SkFdCpHY0.png)
The above is a screenshot of what the code explained outputs when run in SageMath. Notice that when we print the direct output of our Gröbner basis, it gives us the roots in terms of the Riemann Zeta function, where ```zeta(9)^x``` = $(e^{\frac{2\pi i} {9}})^x$. The equivalent integer from 1 to 9 for each of these values is stated in our bijection table, and the corrected output is printed below in the screenshot as well. If you'd like to try the code yourself, go to https://sagecell.sagemath.org/, and copy and paste the code snippets above!

### Boolean System

#### The Model
Another system that effectively models the 9x9 Sudoku puzzle is the boolean system where <span style="color:dodgerblue">binary variables</span> are used to determine if the square takes on a certain value out of ${1, 2,..., 9}$.
For each square slot $x$ in a 9x9 puzzle, the possible input values can be represented with boolean values such that:
<span style="color:dodgerblue">
\begin{align*}
x_{i,j,k} = \begin{cases}
1, & \text{if $x_{ijk}=k$, val at row $i$ and column $j = k$}\\
0, & \text{Otherwise}
\end{cases}\\
\text{for  $\space i, j, k = 1, 2, ...  9$}
\end{align*}</span>
This entails 9 variables for each of the 9x9 = 81 squares, adding up to a total of 729 binary variables to keep track of, which is a lot more than other methods introduced.
	<p style="text-align: center"><img align="" width="450" height="" src="https://hackmd.io/_uploads/S1-gxJAOR.png">

Let's define the constraints we need for this model.
	1. For each <span style="color:dodgerblue">individual slot $x_{ij}$</span>, we must have that:
<span style="color:dodgerblue">\begin{align*}
\sum_{k=1}^9{x_k} = 1
\end{align*}</span>
2. For <span style="color:dodgerblue">each 9 values $k$</span> takes on, all relevant slots in <span style="color:dodgerblue">each **row**, **column**, and **3x3 square**</span> must have that:
<span style="color:dodgerblue">\begin{align*}
\sum_{i=1}^9\sum_{j=1}^9{x_{ijk}} = 1
\end{align*}</span><span style="color:dodgerblue">\begin{align*}
\sum_{j=1}^9\sum_{i=1}^9{x_{ijk}} = 1
\end{align*}</span>
3. For<span style="color:dodgerblue"> every pair of slots $x$ and $w$ in any **row**, **column**, and **3x3 square**</span> of a 9x9 puzzle, we must have that the values they take on do not overlap:
<span style="color:dodgerblue">\begin{align*}
\sum_{k=1}^9{x_k}{w_k} = 0
\end{align*}</span>
	<span style="color:dodgerblue">Either $x_k = 0$ or $w_k = 0$ for every $k$.</span>

#### The Implementation

1. Set up <span style="color:dodgerblue">polynomial ring for our Ideal</span>, accounting for $9*9*9 = 729$ variables. Define and set up our starting puzzle.
```python
import itertools
		
R = PolynomialRing(GF(2), 'x', 729)
x = R.gens()

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

2. Start creating our set of polynomial equations for our Ideal. Given a starting puzzle, add the solution set of equations to be equal to 0 for <span style="color:dodgerblue">existing values</span> already in the board. These defining polynomials are added to set of equations.

<span style="color:dodgerblue">\begin{align*}
(x_{ijk} - 1) = 0\text{ if $x_{ijk} = k$}\\
(x_{ijk}) = 0\text{ if $x_{ijk} \not= k$}
	\end{align*}</span>

```python
equations = []

for i in range(9):
    for j in range(9):
        if puzzle[i][j] != 0:
            rang = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            k = puzzle[i][j] - 1                        
            rang.remove(k)
            equations.append(x[i*81 + j*9 + k] - 1)
            for u in rang:
                equations.append(x[i*81 + j*9 + u])

```
3. Add pair constraints. Apply them to all pairs in every row, column and 3x3. These constraint polynomials are also added to our set of equations.
<span style="color:dodgerblue">\begin{align*}
\sum_{k=1}^9{x_k}{w_k} = 0
\end{align*}</span>
```python
def constraints(a, b):
    sum = 0
    for k in range(9):
        sum += x[81*(a // 9) + 9*(a % 9) + k] * x[81*(b // 9) + 9*(b % 9) + k]
    return sum

for i in range(9):
    row = [i*9 + j for j in range(9)]
    for a, b in itertools.combinations(row, 2):
        equations.append(constraints(a, b))

for j in range(9):
    col = [i*9 + j for i in range(9)]
    for a, b in itertools.combinations(col, 2):
        equations.append(constraints(a, b))

for block_row in range(3):
    for block_col in range(3):
        block = [block_row*27 + block_col*3 + 9*i + j for i in range(3) for j in range(3)]
        for a, b in itertools.combinations(block, 2):
            equations.append(constraints(a, b))

```
4. Add constraints for every $x_{ij}$ such that the sum of the 9 corresponding binary variables will always equal to 1 for each row, column, and $3$x$3$ block. These constraint polynomials are also added to our set of equations.
<span style="color:dodgerblue">\begin{align*}
\sum_{k=1}^9{x_{ijk}} - 1 = 0
\end{align*}</span>
```python
# Each cell contains exactly one number: sum of all booleans is 1 for each cell
for i in range(9):
    for j in range(9):
        cons = sum(x[i*81 + j*9 + k] for k in range(9)) - 1
        equations.append(cons)

# Each num appears exactly once in each row: for every row the sum of all booleans for some value k is 1
for i in range(9):
    for k in range(9):
        cons = sum(x[i*81 + j*9 + k] for j in range(9)) - 1
        equations.append(cons)

# Each num appears exactly once in each column: for every column the sum of all booleans for some value k is 1
for j in range(9):
    for k in range(9):
        cons = sum(x[i*81 + j*9 + k] for i in range(9)) - 1
        equations.append(cons)

# Each num appears exactly once in each 3x3 block: for every block the sum of all booleans for some value k is 1
for row in range(3):
    for col in range(3):
        for k in range(9):
            cons = sum(x[(block_row*3 + i)*81 + (block_col*3 + j)*9 + k]
                        for i in range(3) for j in range(3)) - 1
            equations.append(cons)

```
5. Given all our defining polynomials: <span style="color:dodgerblue">Generate the Ideal and Gröbner basis corresponding to the constraint polynomials.</span> The Gröbner basis distinguished the <span style="color:dodgerblue">81 boolean variables</span> that are true. This is to be mapped into the solved Sudoku puzzle.
```python      
I = R.ideal(list(equations))
G = I.groebner_basis()

bool = [[0 for _ in range(9)] for _ in range(9)]
solution = [[0 for _ in range(9)] for _ in range(9)]
for g in G:
    var = g.variables()[0]
    if g - var == 1:
        index = int(str(var).strip('x'))
        i = index // 81
        j = (index % 81) // 9
        k = index % 9
        solution[i][j] = k + 1
        bool[i][j] = g
```
6. Results when run on https://sagecell.sagemath.org/:
![Screenshot 2024-07-30 090408](https://hackmd.io/_uploads/B1S1Wd8FC.png)

The resulting Ideal is generated by 1332 generators. Out of 729 elements in the Gröbner basis, the 81 binary variables corresponding to the solution set were represented in a distinct way: <span style="color:dodgerblue">$x_{ijk} + 1$</span>. These are easily converted to their respective values and positions in the solved puzzle! This can be done with any starting puzzle with a solution.

## References
[1] textbook
[2] journal article
[3] Image from "Geometric particle swarm optimization for the sudoku puzzle," by A. Moraglio & J. Togelius. (2007). *GECCO '07: Proceedings of the 9th annual conference on Genetic and evolutionary computation*, pp. 118-125. Association for Computing Machinery. https://doi.org/10.1145/1276958.1276975.
