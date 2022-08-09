program main
implicit none
integer::istat,n
character(len=150)::smile
character(len=200)::cmdstr
character(len=30)::filename
character(len=5)::cha
character(len=6)::cha2
real(kind=8)::score
n=0
open(11,file='result_inhouse_fold0.csv')
read(11,*)
do
  read(11,*,iostat=istat) smile,score
  if(istat.ne.0) exit
  n = n+1
  write(cha,'(i5)') n
  write(cha2,'(f6.3)') score
  filename=trim(adjustl(cha))//'.csv'
  open(21,file=filename)
  write(21,'(a5)') 'Smile'
  write(21,'(a)') trim(adjustl(smile))
  close(21)
  cmdstr='chemprop_interpret --data_path '//trim(adjustl(filename))//' &
          --checkpoint_path ../muta_checkpoint_fold/fold_0/model_0/model.pt &
          --property_id 1 --prop_delta '//trim(adjustl(cha2))
  call system(cmdstr)
  write(*,*) cmdstr
enddo
close(11)
end
