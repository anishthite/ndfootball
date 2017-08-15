def quickSort(alist, sortloc):
	   quickSortHelper(alist,0,len(alist)-1, sortloc)

def quickSortHelper(alist,first,last, sortloc):
   if first<last:
	   splitpoint = partition(alist,first,last, sortloc)

	   quickSortHelper(alist,first,splitpoint-1, sortloc)
	   quickSortHelper(alist,splitpoint+1,last, sortloc)


def partition(alist,first,last, sortloc):
   pivotvalue = int(alist[first][sortloc])

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

	   while leftmark <= rightmark and int(alist[leftmark][sortloc]) <= pivotvalue:
		   leftmark = leftmark + 1

	   while int(alist[rightmark][sortloc]) >= pivotvalue and rightmark >= leftmark:
		   rightmark = rightmark -1

	   if rightmark < leftmark:
		   done = True
	   else:
		   temp = alist[leftmark]
		   alist[leftmark] = alist[rightmark]
		   alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
