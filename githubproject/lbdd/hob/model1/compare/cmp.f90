program main
implicit none
integer::i,ncount
real(kind=8)::x(290),y(290)
character(len=200)::bla
open(11,file='test_full.csv')
read(11,*)
do i=1,290
  read(11,*) bla,x(i)
enddo
close(11)
open(21,file='result_3model.csv')
read(21,*)
do i=1,290
  read(21,*) bla,y(i)
enddo
close(21)
ncount=0
do i=1,290
  if(y(i).le.0.5d0.and.abs(x(i)-0.d0).le.1.e-5) ncount=ncount+1
  if(y(i).ge.0.5d0.and.abs(x(i)-1.d0).le.1.e-5) ncount=ncount+1
enddo
write(*,*) ncount
end
