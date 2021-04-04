def findYourOne(males, females, pairs):
    pass


males = ['male1', 'male2', 'male3', 'male4', 'male5', 'male6', 'male7', 'male8', 'male9']
females = ['fem1', 'fem2', 'fem3', 'fem4', 'fem5', 'fem6', 'fem7', 'fem8', 'fem9']

pairs = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,0],[0,1]]
new_pairs = []

for pair in pairs:
    new_pairs.append([males[pair[0]], females[pair[1]]])
print(new_pairs)