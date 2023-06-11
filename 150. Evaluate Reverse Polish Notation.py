#逆ポーランド記法

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            #stackを用意
            stack = []
            #tokensを走査
            while len(tokens) > 0:
                #stackの先頭をポップ
                toke = tokens.pop(0)
                # + なら2つ要素をポップして足し算してスタックに加える
                if toke == "+":
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second+first)
                # - なら2つ要素をポップして引き算してスタックに加える
                #オペランドの順番に注意
                elif toke == "-":
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second-first) #ここが逆にならないように
                # * なら2つ要素をポップして掛算してスタックにいれる
                elif toke == "*":
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second*first)
                #　/ なら2つ要素をポップして割り算してスタックに入れる
                elif toke == "/":
                    first = stack.pop()
                    second = stack.pop()
                    #stack.append(int(float(second)/first))
                    stack.append(int(second/first))
                    
                #数字ならスタックに整数型で入れる
                else:
                    stack.append(int(toke))
            #stackに最後に1つ残っている要素が解答。ポップして返す
            return stack.pop()