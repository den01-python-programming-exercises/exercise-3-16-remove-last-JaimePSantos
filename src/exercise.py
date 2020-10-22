def main():
    #write your code below this line
    strList = ["a","b","c","d"]
    print(strList)
    print(remove_last(strList))

def remove_last(strings):
  print(strings)
  lastRemoved = []
  for i in range((len(strings))):
    if(i==len(strings)-1):
      strings.pop(i)
      return strings
      
if __name__ == '__main__':
    main()
