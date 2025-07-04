import { render, screen } from '@testing-library/react'
import UploadButton from '../../src/components/UploadButton'

describe('UploadButton', () => {
  it('renders with default disabled state', () => {
    render(<UploadButton files={[]} text="" loading={false} />)
    const button = screen.getByRole('button', { name: /Selecione arquivos ou texto/i })
    expect(button).toBeDisabled()
  })

  it('enables and shows correct text when files are provided', () => {
    render(<UploadButton files={[{ name: "file1.txt" }, { name: "file2.txt" }]} text="" loading={false} />)
    const button = screen.getByRole('button', { name: /Enviar 2 arquivo\(s\)/i })
    expect(button).toBeEnabled()
  })

  it('enables and shows correct text when text is provided', () => {
    render(<UploadButton files={[]} text="some email content" loading={false} />)
    const button = screen.getByRole('button', { name: /Enviar texto/i })
    expect(button).toBeEnabled()
  })

  it('displays loading spinner and disables when loading', () => {
    render(<UploadButton files={[]} text="some text" loading={true} />)
    const button = screen.getByRole('button', { name: /Analisando/i })
    expect(button).toBeDisabled()
    expect(screen.getByTestId('spinner')).toBeInTheDocument()
  })
})
