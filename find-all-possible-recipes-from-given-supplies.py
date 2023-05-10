class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        supplies = set(supplies)
        willMake = {recipe: i for i, recipe in enumerate(recipes)}        

        notFound = [0]*n
        comesAfter = defaultdict(list)

        for i  in range(n):
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    if ingredient in willMake:
                        notFound[i] += 1
                        comesAfter[willMake[ingredient]].append(i)
                    else:
                        notFound[i] = -1

        print(notFound)
        que = deque()
        for i in range(n):
            if notFound[i] == 0:
                que.append(i)

        print(que)
        canCreate = []
        while que:
            finished = que.popleft()
            canCreate.append(recipes[finished])

            for i in comesAfter[finished]:
                notFound[i] -= 1
                if notFound[i] == 0:
                    que.append(i)
        
        return canCreate