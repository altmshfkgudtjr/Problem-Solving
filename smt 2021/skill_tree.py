class Skill:
	def __init__(self, name):
		self.name = name
		self.linked = []
	
	# linked 타입: Skill
	def link(self, linked):
		self.linked.append(linked)

skills = list(map(lambda name: Skill(name), input().split()))
n = int(input())
name_list = []
linked_list = []

for i in range(0, n):
	name, linked = input().split()
	name_list.append(name)
	linked_list.append(linked)
	
	target = list(filter(lambda skill: skill.name == name, skills))[0]
	c_target = list(filter(lambda skill: skill.name == linked, skills))[0]
	
	target.link(c_target)

# 단독 스킬 식별
output_list = []
for i in range(0, n):
	if name_list[i] not in linked_list:
		output_list.append(name_list[i])
output_list = list(set(output_list))

# 순환 출력
def print_skill(target, before_string):
	before_string += f' {target.name}'
	if len(target.linked) == 0:
		print(before_string.strip())
		return

	for skill in target.linked:
		print_skill(skill, before_string)

for i in output_list:
	target = list(filter(lambda skill: skill.name == i, skills))[0]
	print_skill(target, "")
	

'''
:::: 입력값 ::::

h g f w r
4
h g
h f
g r
g w
'''

"""
:::: 설명 ::::

인접리스트를 사용해서 문제를 해결한다.
다음과 같이 설정한다.

skills: [ Skill(h), Skill(g), Skill(f), Skill(w), Skill(r) ]

이후 입력을 받으면서 인접리스트를 통해서 각 Skill을 연결시켜준다.

Skill(h) -> [ Skill(g), Skill(f) ]
Skill(g) -> [ Skill(r), Skill(w) ]

이제 연계 스킬이 존재하는 단독스킬을 식별해 준다.

output_list = [ 'h' ]

아래와 같이 DFS를 사용하여 출력한다.

h -> g -> r
       -> w
  -> f

위 과정은 다음과 같이 출력된다.

h g r
h g w
h f

"""