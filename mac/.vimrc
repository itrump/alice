" This line should not be removed as it ensures that various options are
" properly set to work with the Vim-related packages available in Debian.
" debian.vim

" Uncomment the next line to make Vim more Vi-compatible
" NOTE: debian.vim sets 'nocompatible'. Setting 'compatible' changes numerous
" options, so any other options should be set AFTER setting 'compatible'.
set nocompatible

" Vim5 and later versions support syntax highlighting. Uncommenting the
" following enables syntax highlighting by default.
if has("syntax")
  syntax on            " �﷨����
endif
colorscheme ron        " elflord ron peachpuff default ������ɫ������vim�Դ�����ɫ����������/usr/share/vim/vim72/colorsĿ¼��

" detect file type
filetype on
filetype plugin on

" If using a dark background within the editing area and syntax highlighting
" turn on this option as well
set background=dark

" Uncomment the following to have Vim jump to the last position when
" reopening a file
if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
  "have Vim load indentation rules and plugins according to the detected filetype
  filetype plugin indent on
endif

" The following are commented out as they cause vim to behave a lot
" differently from regular Vi. They are highly recommended though.

"set ignorecase        " ����ģʽ����Դ�Сд
"set smartcase        " �������ģʽ������д�ַ�����ʹ�� 'ignorecase' ѡ�ֻ������������ģʽ���Ҵ� 'ignorecase' ѡ��ʱ�Ż�ʹ�á�
set autowrite        " �Զ�������д���ļ�: ����ļ����޸Ĺ�����ÿ�� :next��:rewind��:last��:first��:previous��:stop��:suspend��:tag��:!��:make��CTRL-] �� CTRL-^����ʱ���У��� :buffer��CTRL-O��CTRL-I��'{A-Z0-9} �� `{A-Z0-9} ����ת������ļ�ʱ��Ȼ��
set autoindent        " �����Զ�����(����)����ÿ�е�����ֵ����һ����ȣ�ʹ�� noautoindent ȡ������
"set smartindent        " ���ܶ��뷽ʽ
set tabstop=4        " �����Ʊ��(tab��)�Ŀ��
set softtabstop=4     " �������Ʊ���Ŀ��    
set shiftwidth=4    " (�Զ�) ����ʹ�õ�4���ո�
set cindent            " ʹ�� C/C++ ���Ե��Զ�������ʽ
set cinoptions={0,1s,t0,n-2,p2s,(03s,=.5s,>1s,=1s,:1s     "����C/C++���Եľ���������ʽ
"set backspace=2    " �����˸������
set showmatch        " ����ƥ��ģʽ����ʾƥ�������
set linebreak        " ���ʻ���
set whichwrap=b,s,<,>,[,] " �������׺���ĩʱ����������һ��ȥ
"set hidden " Hide buffers when they are abandoned
set mouse=            " Enable mouse usage (all modes)    "ʹ�����
set number            " Enable line number    "��ʾ�к�
"set previewwindow    " ��ʶԤ������
set history=50        " set command history to 50    "��ʷ��¼50��


"--״̬������--
set laststatus=2 " ����ʾ���һ�����ڵ�״̬�У���Ϊ1�򴰿�������һ����ʱ����ʾ���һ�����ڵ�״̬�У�0����ʾ���һ�����ڵ�״̬��
set ruler            " ��ߣ�������ʾ���λ�õ��кź��кţ����ŷָ���ÿ�����ڶ����Լ��ı�ߡ����������״̬�У������������ʾ����������ʾ����Ļ�����һ���ϡ�

"--����������--
set showcmd            " ��������ʾ���������
set showmode        " ��������ʾvim��ǰģʽ

"--find setting--
set incsearch        " �����ַ�������ʾƥ���
set hlsearch    
set fileencodings=ucs-bom,utf-8,gb2312,cp936,gb18030,big5,euc-jp,euc-kr,latin1,gbk
set expandtab
set list
"set cursorcolumn
