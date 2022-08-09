program main
implicit none
integer::i,x,y,ncount
open(11,file='paper.dat')
ncount=0
do i=1,290
  read(11,*) x,y
  if(x.eq.y) then
    ncount=ncount+1
  else
    write(1001,*) x,y
  endif
enddo
write(*,*) ncount
close(11)
end
