Start
pick secret
while slices>0 and not win:
  show masked word
  get letter; validate
  if repeat -> warn; continue
  if in word -> reveal else slices-1
if win -> saved else sliced
ask replay
