-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 03/10/2024 às 07:11
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `banco tcc`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cadastroanimal`
--

CREATE TABLE `cadastroanimal` (
  `id` int(250) NOT NULL,
  `nome_CadastroAnimal` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `raca_CadastroAnimal` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `especie_CadastroAnimal` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `porte_CadastroAnimal` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `sexo_CadastroAnimal` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `faixa_etaria_CadastroAnimal` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `localizacao_CadastroAnimal` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `descricao_CadastroAnimal` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `foto_CadastroAnimal` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `ong`
--

CREATE TABLE `ong` (
  `id` int(200) NOT NULL,
  `nome_ong` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cnpj_ong` varchar(18) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `estado_ong` varchar(2) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cidade_ong` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `bairro_ong` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `rua_ong` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `email_ong` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `telefone_ong` varchar(15) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `instagram_ong` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `senha_ong` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `ongtelainicial`
--

CREATE TABLE `ongtelainicial` (
  `id` int(11) NOT NULL,
  `nome_pet` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `raca_pet` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `foto_pet` blob DEFAULT NULL,
  `descricao_pet` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `pagamento`
--

CREATE TABLE `pagamento` (
  `id` int(11) NOT NULL,
  `numero_cartao` varchar(16) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nome_titular` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `tipo_cartao` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cpf` varchar(14) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `numero_seguranca` varchar(4) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `senha_cartao` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `produto`
--

CREATE TABLE `produto` (
  `id` int(11) NOT NULL,
  `nome_produto` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `foto_produto` blob DEFAULT NULL,
  `descricao_produto` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `valor_produto` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_adm`
--

CREATE TABLE `tb_adm` (
  `Id` int(3) NOT NULL,
  `Nome` varchar(40) NOT NULL,
  `Email` varchar(60) NOT NULL,
  `Cpf` char(11) NOT NULL,
  `Senha` int(30) NOT NULL,
  `Rsenha` int(30) NOT NULL,
  `Setor` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_adm2`
--

CREATE TABLE `tb_adm2` (
  `Id` int(3) NOT NULL,
  `Nome` varchar(40) NOT NULL,
  `Email` varchar(60) NOT NULL,
  `Cpf` char(11) NOT NULL,
  `Senha` varchar(30) NOT NULL,
  `Rsenha` varchar(30) NOT NULL,
  `Setor` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_ong`
--

CREATE TABLE `tb_ong` (
  `Id` int(3) NOT NULL,
  `Nome` varchar(40) NOT NULL,
  `cnpj` int(18) NOT NULL,
  `Cep` int(9) NOT NULL,
  `Uf` char(2) NOT NULL,
  `Email` varchar(60) NOT NULL,
  `Senha` varchar(3000) NOT NULL,
  `Rsenha` varchar(3000) NOT NULL,
  `Telefone` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_reclamacoes`
--

CREATE TABLE `tb_reclamacoes` (
  `CR` int(3) NOT NULL,
  `Motivo` varchar(40) NOT NULL,
  `Descricao` varchar(350) NOT NULL,
  `Afetado` varchar(50) NOT NULL,
  `id_Afetado` varchar(2) NOT NULL,
  `Acusado` varchar(50) NOT NULL,
  `id_Acusado` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_user`
--

CREATE TABLE `tb_user` (
  `Id` int(3) NOT NULL,
  `Nome` varchar(40) NOT NULL,
  `Email` varchar(60) NOT NULL,
  `Senha` varchar(3000) NOT NULL,
  `Rsenha` varchar(3000) NOT NULL,
  `cidade` varchar(60) NOT NULL,
  `Uf` char(2) NOT NULL,
  `Cpf` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nome_usuario` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cpf_usuario` varchar(14) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `email_usuario` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cidade_usuario` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `uf_usuario` varchar(2) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `senha_usuario` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cadastroanimal`
--
ALTER TABLE `cadastroanimal`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `ong`
--
ALTER TABLE `ong`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `ongtelainicial`
--
ALTER TABLE `ongtelainicial`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `pagamento`
--
ALTER TABLE `pagamento`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `tb_adm`
--
ALTER TABLE `tb_adm`
  ADD PRIMARY KEY (`Id`);

--
-- Índices de tabela `tb_adm2`
--
ALTER TABLE `tb_adm2`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Cpf` (`Cpf`);

--
-- Índices de tabela `tb_ong`
--
ALTER TABLE `tb_ong`
  ADD PRIMARY KEY (`Id`);

--
-- Índices de tabela `tb_reclamacoes`
--
ALTER TABLE `tb_reclamacoes`
  ADD PRIMARY KEY (`CR`);

--
-- Índices de tabela `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`Id`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cadastroanimal`
--
ALTER TABLE `cadastroanimal`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `ong`
--
ALTER TABLE `ong`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `ongtelainicial`
--
ALTER TABLE `ongtelainicial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `pagamento`
--
ALTER TABLE `pagamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `produto`
--
ALTER TABLE `produto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tb_adm`
--
ALTER TABLE `tb_adm`
  MODIFY `Id` int(3) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tb_ong`
--
ALTER TABLE `tb_ong`
  MODIFY `Id` int(3) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tb_reclamacoes`
--
ALTER TABLE `tb_reclamacoes`
  MODIFY `CR` int(3) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tb_user`
--
ALTER TABLE `tb_user`
  MODIFY `Id` int(3) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
